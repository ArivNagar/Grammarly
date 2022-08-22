from textblob import TextBlob
a = TextBlob("Helwo i am a goed robot")
a = a.correct()
print(a)
