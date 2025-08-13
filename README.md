# r_python_decision_tree-mit

R と Python の決定木を比較・再現するサンプルリポジトリです。  
R (`rpart`) と Python (`scikit-learn`) の違いや特徴を理解しながら、決定木の基本的な使い方を学べます。

---

# 概要

- 顧客属性から購入した車のメーカーを予測する決定木モデルを作成
- Python と R で作成した決定木を比較
- 特徴量重要度の違いや、枝刈り・分割条件の挙動を学べる

---

## フォルダ構成
```
├─ 1_flow/
│ ├─ run_decision_tree.py # Python 実行スクリプト
│ └─ run_decision_tree.R # R 実行スクリプト
├─ 2_data/
│ └─ sample.csv # サンプルデータ
├─ 3_output/ # 決定木出力画像用（自動作成）

```
## Python版
Python3系が必要です。  

必要なパッケージは以下のコマンドでインストールしてください。
```
pip install pandas, scikit-learn, matplotlib, japanize_matplotlib
```

### 使い方
このスクリプトは、コマンドライン操作なしで、ファイルをダブルクリックするだけで実行できます。

‐ データ読み込み時に UTF-8/CP932 自動判定
‐ 訓練データ・テストデータに分割して正解率を表示
‐ 決定木を描画（比率あり/なし）して 3_output に PNG 保存
‐ クラス凡例を自動で追加


## R版
RGui または RStudio
```
rpart, rpart.plot
```
### 使い方
```
source("1_flow/run_decision_tree.R")
```

‐ データ読み込み時に UTF-8/CP932 自動判定
‐ 訓練データ・テストデータに分割して正解率を表示
‐ 決定木を描画（比率あり/人数のみ）して 3_output に PNG 保存


# 入力データフォーマット例
2_data/sample.csv を参照ください。


# 比較と考察
‐ 正解率はデータによって異なるが、両方とも主要特徴量は概ね一致（income, age が重要）
‐ Python は scikit-learn の仕様で枝を伸ばしてから制限、R は自動枝刈り
‐ 実務では完全一致させる必要はなく、状況に応じて使い分けるのが現実的

## LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)








