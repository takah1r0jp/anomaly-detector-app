from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
from utils.code_generator import generate_anomaly_detection_code
from utils.code_executor import execute_code

# FastAPIインスタンス作成
app = FastAPI()

# アプリケーション確認用
@app.get("/")
def read_root():
    return {"message": "Welcome to the Anomaly Detection API!"}


# 画像をアップロードして異常検知を行うエンドポイント
@app.post("/detect")
async def detect_anomaly(
    file: UploadFile = File(...),  # 画像ファイルのアップロード
    normal_conditions: str = "画像における正常条件を入力",  # 正常条件のテキスト
):
    try:
        # プロジェクト内の相対パスにtemp_filesディレクトリを作成
        temp_dir = os.path.join(os.path.dirname(__file__), "temp_files")
        os.makedirs(temp_dir, exist_ok=True)

        # 画像ファイルを一時的に保存
        temp_filename = os.path.join(temp_dir, f"temp_{file.filename}")
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ここで異常検知を行うロジックを実装
        # 生成されるまで次の処理に進まないようにする
        
        code = await generate_anomaly_detection_code(normal_conditions)

        result = execute_code(code, temp_filename)

        return {"status": "success", "result": result, "code": code}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    finally:
        # 一時的な保存ファイルを削除
        print("Cleaning up temporary files...")
        cleanup_temp_files(temp_filename)


# サーバーを起動するためのコマンド（後で実行）
# uvicorn app.main:app --reload


def cleanup_temp_files(file_path: str):
    try:
        """使い終わったファイルを削除する関数"""
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
