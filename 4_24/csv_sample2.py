import csv

csv_file = open("resource/titanic3.csv", "r", encoding="ms932")
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる

    # print('小文字に変換した文字列')
    # print(row[2].lower())

    # print('大文字に変換した文字列')
    # print(row[2].upper())

    # fare列を小数点以下で丸める
    n = row[8]
    m = round(float(n))
    print(m)

# もろもろの処理の後、close
csv_file.close()
