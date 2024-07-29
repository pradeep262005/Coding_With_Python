num_words=0
with open ('C:/Users/PRADEEP/Documents/asd.txt','r')as f:
 for line in f:
     words=line.split()
     num_words+=len(words)
     print("num of words:")
     print(num_words)

