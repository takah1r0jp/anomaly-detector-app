FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 依存関係のインストール
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# PyTorch with CUDA
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# アプリケーションコードのコピー
COPY . .

# 環境変数の設定
ENV PORT=8080

# アプリケーションの起動
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
