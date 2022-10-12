from filtration import SentenceToWordFiltration


class WordFreqVector:

  def __init__(self, dictWords):
    self.__dictWords = dictWords
    self.__file = ''
    self.__fileName = ''
    self.__vectorArr = []
    self.__isTrue = False

  def getData(self, file, fileName):
    self.__file = file
    self.__fileName = fileName

  def initialization(self):
    if self.__isTrue == False:
      temp = ['File Name & info(row) x Words(column)']
      allWords = []
      for each in self.__dictWords:
        allWords.append(each)

      temp.extend(allWords)
      self.__vectorArr.append(temp)
      self.__isTrue = True
    self.__createVector()

  def returnData(self):
    if len(self.__vectorArr) != 0:
      return self.__vectorArr
    else:
      return 'Null'

  def __createVector(self):
    filterX = SentenceToWordFiltration()
    temp = [self.__fileName + '\n' + self.__file.split('Description:')[0]]
    wordsFreq = [0] * len(self.__dictWords)
    filterX.getData(self.__file.split('Description:')[1])
    words = filterX.returnData()

    for each in words:
      if each.lower() in self.__dictWords:
        index = self.__dictWords[each.lower()]
        wordsFreq[index - 1] = 1

    temp.extend(wordsFreq)
    self.__vectorArr.append(temp)
