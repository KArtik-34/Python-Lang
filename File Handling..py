 # writing a file 
f=open('making a file.txt','w')
f.write('name = kartikay class = 12  section = A' )
f.close()


#reading a text file with read mode
f=open('making a file.txt','r')
print (f.read ())
f.close()


#reading a text file without reading mode (a+) appending mode
f=open('making a file.txt','a+')
print(f.read())
f.write('\nschool name = don bosco sr sec school')
f.close()