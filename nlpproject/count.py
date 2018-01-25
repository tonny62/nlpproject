import os.path

uncounted_path  = "../corpus/2_unsorted/"
counted_path    = "../corpus/3_unsorted/"

uncounted_files = os.listdir(uncounted_path)

for uncounted_file in uncounted_files :
    #print("reading file: %s" % (uncounted_file))
    sorted_file = open(os.path.dirname(__file__) + "/"+uncounted_path+uncounted_file, 'r', encoding="UTF-8")
    counted_file = open(os.path.dirname(__file__) + "/"+counted_path+uncounted_file, 'w', encoding="UTF-8")
    words = {}
    read_line = sorted_file.readline()
    while read_line :
        word = read_line.strip("\n")
        if read_line != "\n" :
            #print("read: %s" % (word))
            if word in words :
                words[word] = words[word]+1
                #print("word: %s \tcount: %d" % (word,words[word]))
            else:
                #print("add new word: %s" % (word))
                words[word] = 1
        read_line = sorted_file.readline()
    for word in words :
        #print("word: %s \tcount: %d" % (word,words[word]))
        counted_file.write("%s %d\n" % (word,words[word]))
    sorted_file.close()
    counted_file.close()
print("[+] Counting completed!")


