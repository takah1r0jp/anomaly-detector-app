# 画像とテキストを引数に，異常検知コードを自動生成
# 生成したコードを実行して，異常検知
# 結果：異常か正常か，異常な場合その説明（入力されたテキストに準拠）

import os
from google import genai
from google.genai import types
from utils.template_prompt import prompt


def main():
    normal_conditions = """
    Create 1 python function.
    Do not output anything except execute_command()
        
    Normal condition: There are two apples.
    Function:

    """
    final_prompt = prompt + normal_conditions

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=final_prompt,
        config=types.GenerateContentConfig(
            system_instruction="you are python code generator.",
            max_output_tokens=4000,
        ),
    )

    print(response.text)


# 異常検知プログラムの自動生成
async def generate_anomaly_detection_code(normal_conditions: str) -> str:  # text: str >> code: str
    # ここで異常検知を行うロジックを実装
    # テキストを使って異常検知のコードを生成する
    # ここではダミーのコードを返す

    # normal_conditionsがstr型であることを確認
    if not isinstance(normal_conditions, str):
        raise ValueError("normal_conditions must be a string")

    final_condition = f"""
    Create 1 python function.
    Do not output anything except execute_command()
        
    Normal condition:{normal_conditions}
    Function:
    """

    final_prompt = prompt + final_condition

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=final_prompt,
        config=types.GenerateContentConfig(
            system_instruction="you are python code generator",
            max_output_tokens=4000,
        ),
    )

    code = response.text
    print(code)

    with open("generated_code.py", "w") as o:
        print('code="""', file=o)
        print(code, file=o)
        print('"""', file=o)

    # code = """
    # def execute_command1(image_path, image):
    #     image_patch = ImagePatch(image)
    #     pushpin_patches = image_patch.find("pushpin")

    #     # Count the number of pushpins
    #     num_pushpins = len(pushpin_patches)
    #     print(f"Number of pushpins is {num_pushpins}")

    #     # Verify if the count matches the condition
    #     required_num = 15
    #     anomaly_score = 0
    #     if num_pushpins != required_num:
    #         anomaly_score += 1

    #     return formatting_answer(anomaly_score)
    # """

    return code


if __name__ == "__main__":
    main()
