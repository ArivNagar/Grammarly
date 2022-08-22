from textblob import TextBlob
a = TextBlob("Hewwo i am a goed robet")
a = a.correct()
print(a)