import os.path
import sys

dictionary_path = "../corpus/3_unsorted/"
dictionary_files = os.listdir(dictionary_path)

def tokenize(sentence,answers=[]) :

    global min_match
    global list_answer

    answer = answers.copy()
    size = len(answer)
    if sentence == "":
        #print(answer)
        match = 0
        for word in answer:
            if check(word):
                match = match+1
        if match < min_match :
            min_match = match
            list_answer = answer
            #print(list_answer)
            #print('='*100)
    else:
        for i in range(len(sentence)):
            if check(sentence[:i + 1]):
                answer.insert(size, sentence[:i + 1])
                tokenize(sentence[i + 1:], answer)
                answer.pop(size)

def check(word):
    match = 0
    firstChar = word[0]
    try :
        dictionary_file = open(os.path.dirname(__file__) + "/"+dictionary_path+firstChar+'.txt', 'r', encoding="UTF-8")

        line = dictionary_file.readline()
        while line :
            read_line = line.split(" ")
            if word == read_line[0]:
                match = 1
                #print("Found "+word)
                break
            line = dictionary_file.readline()
        dictionary_file.close()
    except FileNotFoundError:
        pass
    return match


while True :
    min_match = sys.maxsize
    list_answer = []
    sentence = input("Enter a sentence to tokenize: ")
    tokenize(sentence)
    print(list_answer)

