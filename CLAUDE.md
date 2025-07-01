# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Python 3.12+を使用したKaggleコンペティションプロジェクトです。依存関係の管理には`uv`を使用し、典型的なKaggleコンペティション構造に従っています。

## 開発環境セットアップ

このプロジェクトは`uv`を使用して依存関係を管理しています。依存関係をインストールするには：
```bash
uv sync
```

開発用依存関係（JupyterLabとKaggle CLIを含む）をインストールするには：
```bash
uv sync --group dev
```

## 共通コマンド

### リントとコード品質
```bash
uv run ruff check .
uv run ruff format .
```

### Jupyter Lab
```bash
uv run jupyter lab
```

### Kaggle CLI（認証済みの場合）
```bash
# コンペティション一覧
uv run kaggle competitions list

# データセット一覧
uv run kaggle datasets list

# コンペティションデータをダウンロード
uv run kaggle competitions download -c <competition-name> -p input/

# データセットをダウンロード
uv run kaggle datasets download -d <dataset-name> -p input/

# 提出
uv run kaggle competitions submit -c <competition-name> -f <file-path> -m "<message>"
```

## プロジェクト構造

- `notebooks/` - データ探索とモデル開発用のJupyterノートブック
- `models/` - 保存されたモデルファイル用ディレクトリ
- `input/` - 入力データファイル用ディレクトリ（通常Kaggleからダウンロード）
- `pyproject.toml` - プロジェクト設定と依存関係

## 依存関係

コアMLスタックには以下が含まれています：
- pandas, polars - データ操作
- scikit-learn - ML アルゴリズム
- lightgbm, xgboost - 勾配ブースティング
- optuna - ハイパーパラメータ最適化
- matplotlib, seaborn - 可視化

## 開発メモ

ノートブックを使用する際は、`uv run jupyter lab`を使用して、すべての依存関係が利用可能な正しい環境を確実にアクティベートしてください。

入力データは`input/`ディレクトリに配置してください（通常はKaggleコンペティションやデータセットからダウンロード）。