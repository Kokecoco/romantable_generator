import json
import romkan
import sys


def convert_to_romaji_table(json_data):
    consonant = json_data["consonant"]
    vowel = json_data["vowel"]

    # 出力用のリスト
    output_lines = []

    # 母音の変換
    for con in consonant:
        for vow in vowel:
            # 母音のシーケンス内の 'l' を 'っ' に変換
            vow_sequence = vow["Sequence"].replace("l", "っ")

            # ローマ字をひらがなに変換
            hira_consonant = romkan.to_hiragana(con["Sequence"] + vow_sequence)

            output_lines.append(f"{con['Token']}{vow['Token']}\t{hira_consonant}")

    return output_lines


def save_to_file(output_lines, filename="azik_neo.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")


def load_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# 外部のJSONファイルからデータを読み込む
file_path = sys.argv[1]  # ここにJSONファイルのパスを指定してください
json_data = load_json_file(file_path)

# JSONデータを処理
output_lines = convert_to_romaji_table(json_data)

# 出力ファイルに保存
save_to_file(output_lines)
