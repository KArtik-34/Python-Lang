#Importing CSV
import csv
with open('Student_Details.csv','w',newline='') as csvf:
     writecsv=csv.writer(csvf,delimiter=',')
     choice='y'
     while choice.lower()=='y':
          rl=int(input("Enter Roll No.: "))
          n=input("Enter Name: ")
          p=float(input("Enter Percentage: "))
          r=input("Enter Remarks: ")
          writecsv.writerow([rl,n,p,r])
          print(" Data saved in Student Details file..")
          choice=input("Want add more record(y/n).....")
          
with open('Student_Details.csv','r',newline='') as fileobject:
     readcsv=csv.reader(fileobject)
     for i in readcsv:
          print(i)
