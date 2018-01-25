import sys
sys.setrecursionlimit(2000)
myword = 'สมทรงนม'
global mydict
mydict = ['สมทรง','นม','ใหญ่','มากมาย','น']

def segment(word,start,end):
    if(word[start:end] in mydict):
        return str(word[start:end])+'|'
    else:
        if(start==end):
            return(word[end:])
        else:
            return segment(word,start,end-1)+segment(word,end-1,end)

print(segment(myword,0,len(myword)))