# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import os
import sys
import subprocess
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import japanize_matplotlib  # matplotlibで日本語ラベルを扱うためのライブラリ

# ディレクトリ・ファイル設定
INPUT_FOLDER = '2_data'
INPUT_FILE = 'sample.csv'
OUTPUT_FOLDER = '3_output'

save_name  = 'decision_tree.png'       # 比率あり
non_save_name  = 'decision_tree_N.png' # 比率なし

# 除外カラム設定
ID = 'ID'
cluster = 'cluster'

#目的変数
target_col = 'car' 

# パス設定
current_path = os.getcwd()
parent_path = os.path.dirname(current_path)

input_path = os.path.join(parent_path, INPUT_FOLDER, INPUT_FILE)
output_path = os.path.join(parent_path, OUTPUT_FOLDER)
os.makedirs(output_path, exist_ok=True)  # フォルダがなければ作成

save_path = os.path.join(output_path, save_name)
Non_save_path = os.path.join(output_path, non_save_name)

# CSV読み込み（文字コード自動判定）
try:
    df = pd.read_csv(input_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(input_path, encoding="cp932")

# %%
# 説明変数と目的変数に分ける
X_df = df.drop([ID, cluster, target_col], axis=1)  # cluster列は事前に作成されていると仮定
y_df = df[target_col]  # 目的変数（car）

# 訓練・テストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X_df, y_df, random_state=0)
print(f"学習データ数: {len(X_train)} / テストデータ数: {len(X_test)}")

# 決定木モデル構築
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
model = clf.fit(X_train, y_train)

print(
    f"正解率（train）: {model.score(X_train, y_train):.3f} / "
    f"正解率（test）: {model.score(X_test, y_test):.3f}"
)


# %%
def add_class_legend(legend_text, x=0.02, y=0.98):
    """決定木のクラス凡例をFigureに追加"""
    plt.gcf().text(
        x, y,
        legend_text,
        fontsize=13,
        va="top",
        ha="left",
        bbox=dict(
            boxstyle="round,pad=0.5",
            fc="lightyellow",
            ec="gray",
            lw=1
        )
    )

# クラスインデックス対応表
legend_text = "Class index mapping:\n" + "\n".join(
    [f"{idx}: {label}" for idx, label in enumerate(model.classes_)]
)

# 比率なし
plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X_df.columns,
          class_names=model.classes_.astype(str),
          filled=True, max_depth=6)
add_class_legend(legend_text)
plt.savefig(Non_save_path, dpi=300)
plt.show()

# 比率あり
plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X_df.columns,
          class_names=model.classes_.astype(str),
          filled=True, max_depth=6, proportion=True)
add_class_legend(legend_text)
plt.savefig(save_path, dpi=300)
plt.show()

# 特徴量
for name, importance in zip(X_df.columns, model.feature_importances_):
    print(f"{name}: {importance:.3f}")

# OS別で出力フォルダを開く
if sys.platform.startswith('win'):
    os.startfile(output_path)
elif sys.platform.startswith('darwin'):
    subprocess.run(['open', output_path])
else:
    subprocess.run(['xdg-open', output_path])

print('処理完了')
