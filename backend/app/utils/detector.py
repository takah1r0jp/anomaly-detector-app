# 画像とテキストを引数に，異常検知コードを自動生成
# 生成したコードを実行して，異常検知
# 結果：異常か正常か，異常な場合その説明（入力されたテキストに準拠）

from PIL import Image
import torch
import numpy as np
from transformers import (
    AutoModelForVision2Seq,
    AutoTokenizer,
    AutoImageProcessor,
    StoppingCriteria,
    AutoProcessor,
    AutoModelForZeroShotObjectDetection,
)
import os
import json
from datetime import datetime
import requests

from google import genai

def main():
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works",
    )

    print(response.text)


# 異常検知プログラムの自動生成
def generate_anomaly_detection_code():
    # ここで異常検知を行うロジックを実装
    # 例として、画像とテキストを使って異常検知のコードを生成する
    # ここではダミーのコードを返す

    code = """
    def execute_command1(image_path, image):
        image_patch = ImagePatch(image)
        pushpin_patches = image_patch.find("pushpin")
        
        # Count the number of pushpins
        num_pushpins = len(pushpin_patches)
        print(f"Number of pushpins is {num_pushpins}")
        
        # Verify if the count matches the condition
        required_num = 15
        anomaly_score = 0
        if num_pushpins != required_num:
            anomaly_score += 1
            
        return formatting_answer(anomaly_score)
    """

    return code

if __name__ == "__main__":
    main()