# ① 財布の中に入っているレシートの合計金額を数えるプログラムを書いてください
wallet = []
count = input('レシートの枚数を教えてください : ')

for i in range(int(count)):
    r = input('商品の値段を教えてください : ')
    wallet.append(int(r))


print(f"合計金額は{sum(wallet)}円です")

# ② 日本語をローマ字に変換するプログラムを書いてください
import romkan

# 日本語の文字列をローマ字に変換する例
japanese_text = "こんにちは、元気ですか？"
romaji_text = romkan.to_roma(japanese_text)
print(romaji_text)  # Output: "konnichiwa, genki desu ka?"

# ローマ字を日本語に変換する例
romaji_input = "konnichiwa, genki desu ka?"
japanese_output = romkan.to_hiragana(romaji_input)
print(japanese_output)  # Output: "こんにちは、げんきですか？"

text = "はしめまして"
rote = romkan.to_roma(text)
print(rote)
