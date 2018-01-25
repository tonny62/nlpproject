myword = 'สมทรงนมมากเลย'

mydict = ['สมทรง','มาก','ใหญ่','มากมาย']

list_answer = []
max_match_word = 0
def segment(sentence,answers=[]) :
    answer = answers.copy()
    size = len(answer)
    if sentence == "":
        global max_match_word
        global list_answer
        match = 0
        #print(answer)
        for word in answer :
            if word in mydict :
                #print("Match %s"%(word))
                match = match+1
        #print("Match %d word(s)"%match)
        if match >= max_match_word :
            max_match_word = match
            list_answer=answer
        #print('==============================================')
    else:
        for i in range(len(sentence)):
            answer.insert(size,sentence[:i+1])
            segment(sentence[i+1:],answer)
            answer.pop(size)

segment(myword)

print("Maximum match number: %d"%max_match_word)
print(list_answer)