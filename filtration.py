from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
import nltk

nltk.download('punkt')
nltk.download('stopwords')


class SentenceToWordFiltration:

  def __init__(self):
    self.__textData = ''

  def getData(self, data):
    self.__textData = data
    self.__intoLowercase()
    self.__removePunctuation()
    self.__removeNumericalDigits()
    self.__wordTokenization()
    self.__removeStopwords()
    #self.__spellingCorrection()
  def __str__(self):
    return str(self.__textData)

  def returnData(self):
    if len(self.__textData) != 0:
      return self.__textData
    else:
      return 'Null'

  def __intoLowercase(self):
    self.__textData = self.__textData.lower()

  def __removePunctuation(self):
    symbols = '''!(ˈɪːˈ)-[]{};:'"\,<>./|?@#$%^&*_~�'''
    temp_textData = ''

    for eachSymbol in self.__textData:
      if eachSymbol not in symbols:
        temp_textData += eachSymbol

    self.__textData = temp_textData

  def __removeNumericalDigits(self):
    symbols = '''0123456789'''
    temp_textData = ''

    for eachSymbol in self.__textData:
      if eachSymbol not in symbols:
        temp_textData += eachSymbol

    self.__textData = temp_textData

  def __wordTokenization(self):
    temp_textData = word_tokenize(self.__textData)
    self.__textData = temp_textData

  def __removeStopwords(self):
    stopwordsList = stopwords.words('english')
    temp_textData = []

    for word in self.__textData:
      if word not in stopwordsList:
        temp_textData.append(word)

    self.__textData = temp_textData

  def __spellingCorrection(self):
    temp_textData = []
    correct_words = words.words()

    for word in self.__textData:
      temp = [(jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w)
              for w in correct_words if w[0] == word[0]]
      temp_textData.append(sorted(temp, key=lambda val: val[0])[0][1])

    self.__textData = temp_textData
