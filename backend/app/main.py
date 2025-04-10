from fastapi import FastAPI, File, UploadFile
from typing import Optional
import shutil

# FastAPIインスタンス作成
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Anomaly Detection API!"}

# 画像をアップロードして異常検知を行うエンドポイント
@app.post("/detect")
async def detect_anomaly(
    file: UploadFile = File(...),  # 画像ファイルのアップロード
    normal_conditions: str = "画像における正常条件を入力"  # 正常条件のテキスト
):
    # 画像ファイルを一時的に保存
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ここで異常検知を行うロジックを実装
    result = {"message": "未実装だよ", "is_anomalous": False}

    return {"status": "success", "result": result}

# サーバーを起動するためのコマンド（後で実行）
# uvicorn app.main:app --reload