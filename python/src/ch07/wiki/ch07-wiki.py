import wikipedia
import matplotlib.pylab as plt
from wordcloud import WordCloud, STOPWORDS

wiki = wikipedia.page('Artificial intelligence')

text = wiki.content

s_words = STOPWORDS.union({
  'one', 'using', 'first', 'two', 'make', 'use'
})
wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words).generate(text)

plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.show()
