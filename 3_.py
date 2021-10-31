import time


#reading a text file using a clause for counting no. of characters
with open('making a file.txt','r') as f:
  data=f.readlines()
  for lines in data:
    words=lines.split()
    for word in words:
      for c in word:
        print(c)

time.sleep(5)#for pause between the codes



#reading a text file for counting no. of characters in an easy way 
with open('making a file.txt','r') as f:
  c=''
  while 1:
    c=f.read(1)
    if not c:
      break
    print(c,end="")

time.sleep(5)#for pause between the codes
    

#reading a text file for no. of alpabest and digits
with open('making a file.txt','r') as f:
  c=''
  digit=alpha=0
  while 1:
    c=f.read(1)
    if not c:
      break
    if (c.isdigit()):
       digit+=1
    elif (c.isalpha()):
      alpha+=1
print("\n\n\n\nThere is/are Total" ,digit,"digit(s)")
print("\nThere is/are Total" ,alpha,"alphabet(s)")
