class node:
    def __init__(self, word, reststring):
        self.word = word
        self.reststring = reststring
        self.childlist = []
        self.genchild()

    def genchild(self):
        for i in range(1, len(self.reststring) + 1):
            ## rule
            if (self.reststring[0:i] in mydict):
                tempnode = node(self.reststring[0:i], self.reststring[i:])
                self.childlist.append(tempnode)
            else:
                pass
        ## jump

    def __str__(self):
        return 'Word : ' + str(self.word) + ' \nRest string : ' + str(self.reststring)


word = ''
reststring = 'สมทรงนม'

global mydict
mydict = ['สมทรง', 'นม', 'ใหญ่', 'สม']

root = node(word, reststring)
print(root)
