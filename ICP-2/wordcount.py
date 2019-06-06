fileName = input("Enter file name : ")
f = open(fileName,'r')
wordcount={}
for str in f.read().split():
    if str not in wordcount:
        wordcount[str] = 1
    else:
        wordcount[str] += 1
print(str,wordcount)

