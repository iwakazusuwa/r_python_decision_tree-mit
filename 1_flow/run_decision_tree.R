#----------------------------------------------
# ライブラリ
#----------------------------------------------
library(rpart)
library(rpart.plot)

#----------------------------------------------
# ディレクトリ・ファイル設定（親ディレクトリ基準）
#----------------------------------------------
current_path <- getwd()
parent_path <- dirname(current_path)

INPUT_FOLDER  <- "2_data"
OUTPUT_FOLDER <- "3_output"
INPUT_FILE    <- "sample.csv"

input_path  <- file.path(parent_path, INPUT_FOLDER, INPUT_FILE)
output_path <- file.path(parent_path, OUTPUT_FOLDER)

if (!dir.exists(output_path)) dir.create(output_path)

# 出力ファイル名
save_name     <- file.path(output_path, "R_decision_tree.png")    # 比率あり
non_save_name <- file.path(output_path, "R_decision_tree_N.png")  # 人数のみ

#----------------------------------------------
# CSV読み込み（文字コード自動判定）
#----------------------------------------------
# まずUTF-8で読み込み、失敗したらCP932（Shift-JIS）で
df <- tryCatch({
  read.csv(input_path, fileEncoding = "UTF-8")
}, error = function(e) {
  read.csv(input_path, fileEncoding = "CP932")
})

#----------------------------------------------
# 除外カラム設定・目的変数
#----------------------------------------------
ID <- "ID"
cluster <- "cluster"
target_col <- "car"

x_df <- df[, setdiff(names(df), c(ID, cluster, target_col))]
y_df <- df[[target_col]]

# rpart用に結合
data_all <- data.frame(y_df, x_df)

#----------------------------------------------
# 訓練・テストデータ分割（75% / 25%）
#----------------------------------------------
set.seed(0)  # 再現性確保
train_idx <- sample(seq_len(nrow(data_all)), size = 0.75 * nrow(data_all))
train_data <- data_all[train_idx, ]
test_data  <- data_all[-train_idx, ]



#----------------------------------------------
# 決定木モデル構築（max_depth=3）
#----------------------------------------------
model <- rpart(y_df ~ ., 
               data = train_data, 
               method = "class", 
               parms = list(split = "gini"),
               control = rpart.control(maxdepth = 3))

# 正解率計算
train_pred <- predict(model, train_data, type = "class")
train_acc <- mean(train_pred == train_data$y_df)

test_pred <- predict(model, test_data, type = "class")
test_acc <- mean(test_pred == test_data$y_df)

cat(sprintf("学習データ数: %d / テストデータ数: %d\n", nrow(train_data), nrow(test_data)))
cat(sprintf("正解率（train）: %.3f / 正解率（test）: %.3f\n", train_acc, test_acc))

#----------------------------------------------
# 決定木作成（全データ, maxdepth=6）
#----------------------------------------------
model_full <- rpart(y_df ~ ., 
                    data = data_all, 
                    method = "class", 
                    parms = list(split = "gini"),
                    control = rpart.control(maxdepth = 6))

#----------------------------------------------
# 特徴量
#----------------------------------------------
print(model$variable.importance)

#----------------------------------------------
# 決定木プロット（比率あり） & PNG保存
#----------------------------------------------
png(save_name, width = 1000, height = 800)
rpart.plot(model_full, type = 2, extra = 104, fallen.leaves = TRUE, main = "決定木(比率)")
dev.off()

#----------------------------------------------
# 決定木プロット（人数のみ） & PNG保存
#----------------------------------------------
png(non_save_name, width = 1000, height = 800)
rpart.plot(model_full, type = 2, extra = 1, fallen.leaves = TRUE, main = "決定木（人数のみ）")
dev.off()

cat("処理完了\n")

