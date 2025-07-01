# kg

Kaggleコンペティション用のPythonプロジェクト

## クイックスタート

```bash
# 依存関係をインストール
uv sync --group dev

# Jupyter Labを起動
uv run jupyter lab
```

## プロジェクト構造

- `notebooks/` - データ分析・モデル開発用ノートブック
- `input/` - 入力データ（Kaggleからダウンロード）
- `models/` - 訓練済みモデル保存用

## 主要な依存関係

pandas, scikit-learn, lightgbm, xgboost, optuna