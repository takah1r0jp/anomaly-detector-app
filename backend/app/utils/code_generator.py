# 画像とテキストを引数に，異常検知コードを自動生成
# 生成したコードを実行して，異常検知
# 結果：異常か正常か，異常な場合その説明（入力されたテキストに準拠）

import os
# from google import genai
# from google.genai import types
from app.utils.template_prompt import prompt 
import anthropic


def main():
    normal_conditions = """
    Create 1 python function.
    Do not output anything except execute_command()
        
    Normal condition: There are two apples.
    Function:

    """
    final_prompt = prompt + normal_conditions

    # Anthropic

    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
    )

    message = client.messages.create(
        max_tokens=4000,
        messages=[{"role": "user", "content": final_prompt}],
        model="claude-3-7-sonnet-20250219",
    )
    print(message.content[0].text)


    # Gemini
    # client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    # response = client.models.generate_content(
    #     model="gemini-1.5-pro",
    #     contents=final_prompt,
    #     config=types.GenerateContentConfig(
    #         system_instruction="you are python code generator.",
    #         max_output_tokens=4000,
    #     ),
    # )

    # print(response.text)


# 異常検知プログラムの自動生成
async def generate_anomaly_detection_code(normal_conditions: str) -> str:  # text: str >> code: str
    # テキストを使って異常検知のコードを生成する

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

    # Anthropic
    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
    )

    message = client.messages.create(
        max_tokens=4000,
        messages=[{"role": "user", "content": final_prompt}],
        model="claude-3-7-sonnet-20250219",
    )
    code = message.content[0].text
    print(code)
    
    # Gemini
    # client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    # response = client.models.generate_content(
    #     model="gemini-1.5-pro",
    #     contents=final_prompt,
    #     config=types.GenerateContentConfig(
    #         system_instruction="you are python code generator",
    #         max_output_tokens=4000,
    #     ),
    # )
    # code = response.text
    # print(code)

    with open("generated_code.py", "w") as o:
        print('code="""', file=o)
        print(code, file=o)
        print('"""', file=o)

    return code


if __name__ == "__main__":
    main()
