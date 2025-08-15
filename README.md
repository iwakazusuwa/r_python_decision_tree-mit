# r_python_decision_tree-mit

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0+-blue)](https://www.r-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

R (`rpart`) と Python (`scikit-learn`) の決定木モデルを比較・再現するサンプルリポジトリです。  
顧客属性から購入した車のメーカーを予測するモデルを通じて、両言語の特徴や挙動の違いを学べます。

---

## 対象者

- R と Python の決定木モデルの挙動や特徴の違いを比較したい方
- 決定木の基本的な使い方を学びたい方
- 特徴量重要度や枝刈り、分割条件の挙動を理解したい方

---

## 概要

このリポジトリでは、以下の内容を学べます：

- 顧客属性データを用いて、購入した車のメーカーを予測する決定木モデルの構築
- R (`rpart`) と Python (`scikit-learn`) によるモデルの比較
- 特徴量重要度の違いや、枝刈り・分割条件の挙動の違いの理解

---

## 特徴

- R と Python の両方で決定木モデルを実装
- 特徴量重要度や枝刈りの挙動を比較
- 分割条件の違いや、モデルの解釈性を学習

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


---

## インストール
### Python

Python 3.10 以降が必要です。

必要なパッケージは以下のコマンドでインストールしてください：

```bash
pip install pandas scikit-learn matplotlib japanize_matplotlib
```

### R
R 4.0 以降が必要です。
必要なパッケージは以下のコマンドでインストールしてください：
```R
install.packages("rpart")
install.packages("rpart.plot")
```

# 使い方
## Python
1. 2_data/sample.csv に分析したい顧客データを準備してください。
2. 以下のコマンドでスクリプトを実行します：
```
python 1_flow/run_decision_tree.py
```

3. 結果は 3_output/ フォルダに以下のファイルとして保存されます：
   - decision_tree.png：決定木画像
   - feature_importance.csv：特徴量重要度の CSV ファイル

## R版
1. 2_data/sample.csv に分析したい顧客データを準備してください。
2. 以下のコマンドでスクリプトを実行します：
```
source("1_flow/run_decision_tree.R")
```
3. 結果は 3_output/ フォルダに以下のファイルとして保存されます：
   - decision_tree.png：決定木画像
   - feature_importance.csv：特徴量重要度の CSV ファイル


# 入力データフォーマット例
2_data/sample.csv を参照ください。


# 特記事項
 - 入力データのカラム名や形式が異なる場合、スクリプト内の設定を変更してください。
 - Python と R でのモデルの挙動や出力が異なる場合があります。詳細は各スクリプト内のコメントをご参照ください。

# 今後の展望
 - 他の機械学習アルゴリズムとの比較機能の追加
 - モデルの性能評価指標（例：精度、F1スコア）の比較機能の追加
 - 可視化機能の拡充（例：インタラクティブな可視化）

# 貢献方法
プロジェクトへの貢献は以下の方法で歓迎します：
 - バグ報告や機能追加の提案は Issues で
 - コード改善や新機能追加は Pull Request で
 - ドキュメント改善や翻訳も歓迎

## LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)








