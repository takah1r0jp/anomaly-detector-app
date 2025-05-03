FROM python:3.9-slim

WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY . .

# 環境変数の設定
ENV PORT=8080

# アプリケーションの起動
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
