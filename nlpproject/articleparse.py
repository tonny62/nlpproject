import os

os.chdir('../corpus')
article_filelist = os.listdir('article')

ignoredlist = [' ', '(', ')', ',', ':', ';', '\"', '\'']

for file in article_filelist:
    filename = 'article/'+str(file)
    myfile = open(filename, encoding='utf8', mode='r')
    for line in myfile:
        splitted_line = line.split(sep='|')
        for word in splitted_line:
            if (word in ignoredlist):
                pass
            else:
                filenamein = '1_unsorted/'+ str(word[0]) + '.txt'
                wfile = open(filenamein, mode='a', encoding='utf8')
                wfile.write(word+'\n')
                wfile.close()

