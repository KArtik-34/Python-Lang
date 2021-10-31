import time
#reading a text file line wise
f=open('making a file.txt','r')
count=1
for c in f:
  print("count=",count,c)
  count+=1 
f.close()

time.sleep(3) #for pause between the codes


#reading a text file using a clause for splitting words
f=open('making a file.txt','r')
data=f.readlines()
for lines in data:
    words=lines.split()
    print(words)
f.close()
  
time.sleep(3)


#reading a text file using a clause for counting no. of words
f=open('making a file.txt','r')
data=f.readlines()
no_of_words=0
for lines in data:
    words=lines.split()
    for word in words:
      no_of_words+=1
      print(word)
      print("The File has Total" ,no_of_words,"words")
f.close()
  


    
      
       