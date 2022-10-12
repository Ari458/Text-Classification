class DictionaryMaker:
    def __init__(self):
        self.__textData=[]
        self.__count=0
        self.__dictWords={}
    def getData(self,data):
        self.__textData=data
        self.__dictMake()
    def returnData(self):
        if len(self.__dictWords)!=0:
            return self.__dictWords
        else:
            return 'Null'  
    def __str__(self):
        return str(self.__dictWords)
    def __counter(self):
        self.__count+=1
        return self.__count
    def __dictMake(self):
        for word in self.__textData:
            if word not in self.__dictWords:
                self.__dictWords[word]=self.__counter()


