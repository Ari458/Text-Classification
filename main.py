import wordFrequency as wf
import filtration as fl
import dictionary as dic
import os
import json
import csv

directoryPath = 'data(input)'
allFiles = os.listdir(directoryPath)
filterX = fl.SentenceToWordFiltration()
dictX = dic.DictionaryMaker()

bow = {}

for file in allFiles:
  rawData = open(directoryPath + '/' + file,
                 'rt',
                 encoding="ascii",
                 errors="replace").read().split('Description:')[1]
  filterX.getData(rawData)
  filterData = filterX.returnData()
  dictX.getData(filterData)

saveDataText = open('bag of words(output)/bow.txt',
                    'w+',
                    encoding="ascii",
                    errors="replace")
saveDataText.seek(0)
saveDataText.truncate()
saveDataText.write(str(dictX.returnData()))
saveDataText.close()

saveDataJSON = open('bag of words(output)/bow.json',
                    'w+',
                    encoding="ascii",
                    errors="replace")
saveDataJSON.write(json.dumps(dictX.returnData(), indent=4))
saveDataJSON.close()

vectorX = wf.WordFreqVector(dictX.returnData())
for file in allFiles:
  rawData = open(directoryPath + '/' + file,
                 'rt',
                 encoding="ascii",
                 errors="replace").read()
  vectorX.getData(rawData, file)
  vectorX.initialization()

saveDataVector = open('word frequency vector(output)/vector.txt',
                      'w+',
                      encoding="ascii",
                      errors="replace")
saveDataVector.seek(0)
saveDataVector.truncate()
saveDataVector.write(str(vectorX.returnData()))
saveDataVector.close()

with open('word frequency vector(output)/vector.csv',
          'w+',
          encoding="ascii",
          errors="replace") as my_csv:
  csvWriter = csv.writer(my_csv, delimiter=',')
  csvWriter.writerows(vectorX.returnData())

print('done')
