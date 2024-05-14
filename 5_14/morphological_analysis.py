import MeCab
# wakati = MeCab.Tagger("-Owakati")
# wakati.parse("pythonが大好きです").split()
# tagger = MeCab.Tagger()
# print(tagger.parse("pythonが大好きです"))

text = '''山路を登りながら、こう考えた。
智に働けば角が立つ。情に棹させば流される。意地を通せば窮屈だ。とかくに人の世は住みにくい。
住みにくさが高じると、安い所へ引き越したくなる。どこへ越しても住みにくいと悟った時、詩が生れて、画が出来る。
人の世を作ったものは神でもなければ鬼でもない。やはり向う三軒両隣りにちらちらするただの人である。ただの人が作った人の世が住みにくいからとて、越す国はあるまい。あれば人でなしの国へ行くばかりだ。人でなしの国は人の世よりもなお住みにくかろう。
越す事のならぬ世が住みにくければ、住みにくい所をどれほどか、寛容て、束の間の命を、束の間でも住みよくせねばならぬ。ここに詩人という天職が出来て、ここに画家という使命が降る。あらゆる芸術の士は人の世を長閑にし、人の心を豊かにするが故に尊い。'''

mecabTagger = MeCab.Tagger()
noun_count = {}

node = mecabTagger.parseToNode(text)
while node:
    word = node.surface
    hinshi = node.feature.split(",")[0]
    if word in noun_count.keys() and hinshi == "名詞":
        noun_freq = noun_count[word]
        noun_count[word] = noun_freq + 1
    elif hinshi == "名詞":
        noun_count[word] = 1
    else:
        pass
    node = node.next
    
noun_count = sorted(noun_count.items(), key=lambda x:x[1], reverse=True)
# print(noun_count)

max1_element = sorted(noun_count, key=lambda x: x[1])[-1]
max2_element = sorted(noun_count, key=lambda x: x[1])[-2]

print(max1_element)
print(max2_element)