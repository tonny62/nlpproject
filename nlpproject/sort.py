import os.path

unsorted_path  = "../corpus/1_unsorted/"
sorted_path    = "../corpus/2_unsorted/"

unsorted_files = os.listdir(unsorted_path)

#print(unsorted_files)

for unsorted_file in unsorted_files :
    #print("reading file: %s" % (unsorted_file))
    read_file = open(os.path.dirname(__file__)+"/"+unsorted_path+unsorted_file,'r',encoding="UTF-8")
    lines = []
    read_line = read_file.readline()
    while read_line :
        if read_line != "\n" :
            #print("read: ", read_line)
            lines.append(read_file.readline())
        read_line = read_file.readline()
    read_file.close()
    #print("writing file: %s" % (unsorted_file))
    sorted_file = open(os.path.dirname(__file__)+"/"+sorted_path+unsorted_file,'w',encoding="UTF-8")
    for write_line in sorted(lines) :
        print("write: ",write_line)
        sorted_file.write(write_line)
    sorted_file.close()
print("[+] Sorting completed!")


