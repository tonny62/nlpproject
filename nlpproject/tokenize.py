import os.path
import sys

dictionary_path = "../corpus/3_unsorted/"
dictionary_files = os.listdir(dictionary_path)

list_answer = []


def tokenize(sentence,answers=[],min=sys.maxsize) :

    global list_answer

    answer = answers.copy()
    size = len(answer)
    if sentence == "":
        #print(answer)
        #print('='*100)
        if size<min :
            max_match_word = size
            list_answer = answer
    else:
        for i in range(len(sentence)):
            if check(sentence[:i+1]):
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
                break
            line = dictionary_file.readline()
        dictionary_file.close()
    except FileNotFoundError:
        pass
    return match


while True :
    sentence = input("Enter a sentence to tokenize: ")
    tokenize(sentence)
    print(list_answer)

