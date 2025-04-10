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

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)


