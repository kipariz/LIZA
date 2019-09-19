#functions#
import random
import wikipedia
from langdetect import detect

#false if language is not english
def languageCheck(text):
	if (detect(text)=="en"):
		return True
	else:
		return False

#переделать для поиска первых предложени
#поиск первого предложения в википедии
def wikiSearch(word):
	return(wikipedia.summary(word, sentences=3))

#answer to a "what" type of question
def questionParse(in_data, question): 
    inp = str(question)
    index = in_data.find(inp)
    result = in_data[(index+len(inp)):(len(in_data)-1)]
    return wikiSearch(result)

#detect type of question
def typeQuestion(in_data):
	result = ""
	in_data = str.lower(in_data)
	
	if ("what" and "is" in (in_data.split())):
		result= questionParse(in_data, "what is")
	elif("who" and  "is" in (in_data.split())):
		result= questionParse(in_data, "who is")
	elif("where" and "is" in (in_data.split())):
		result= questionParse(in_data, "where is")
	elif("when" in (in_data.split())):
		result= questionParse(in_data, "when")
	elif("when" and "was" in (in_data.split())):
		result= questionParse(in_data, "when was")

	return result




#проверка последних трех символов на символ вопроса
def isQuestion(in_data):
    len_in_data = len(in_data) - 1
    #string out of range
    if(in_data[len_in_data] == "?" or in_data[len_in_data-1] == "?" or in_data[len_in_data-2] == "?"):
        return True
    else:
        return False
