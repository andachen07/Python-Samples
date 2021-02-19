
year=int(input("輸入年份："))
month = int(input("請輸入月："))


days=[31,28,31,30,31,30,31,31,30,31,30,31]

year1=year-1
totalDays=int(year1*365+year1/4+year1/400-year1/100);

if year%4==0:
      days[1]=29

if month>1:
   totalDays=totalDays+days[0]
if month>2:     
   totalDays=totalDays+days[1]
if month>3:
   totalDays=totalDays+days[2]      
if month>4:     
   totalDays=totalDays+days[3]
if month>5:
   totalDays=totalDays+days[4]
if month>6:
   totalDays=totalDays+days[5]
if month>7:
   totalDays=totalDays+days[6]
if month>8:
   totalDays=totalDays+days[7]
if month>9:
   totalDays=totalDays+days[8]
if month>10:
   totalDays=totalDays+days[9]      
if month>11:
   totalDays=totalDays+days[10]      
if month>12:
   totalDays=totalDays+days[11]      
 
iCount = 0
print ("日\t一\t二\t三\t四\t五\t六")

daynum=totalDays%7+1

if daynum>0:
   print ('\t', end=""); iCount+=1
if daynum>1:
   print ('\t', end=""); iCount+=1
if daynum>2:
   print ('\t', end=""); iCount+=1
if daynum>3:
   print ('\t', end=""); iCount+=1
if daynum>4:
   print ('\t', end=""); iCount+=1
if daynum>5:
   print ('\t', end=""); iCount+=1
if daynum>6:
   print ('\t', end=""); iCount+=1
  
i=1
if (iCount%7==0):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>1):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>2):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>3):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>4):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>5):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>6):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7==0):
    print ("")
  
if (iCount%7==0):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=1):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=2):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=3):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=4):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=5):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=6):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7==0):
    print ("")

if (iCount%7==0):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=1):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=2):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=3):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=4):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=5):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=6):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7==0):
    print ("")

if (iCount%7==0):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=1):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=2):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=3):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=4):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=5):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=6):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7==0):
    print ("")

if  iCount%7==0 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if  iCount%7>=1 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=2 and i<=days[month-1]):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=3 and i<=days[month-1]):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=4 and i<=days[month-1]):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=5 and i<=days[month-1]):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7>=6 and i<=days[month-1]):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if (iCount%7==0):
    print ("")
    
if (iCount%7==0 and i<=days[month-1]):
    print ("%.2i\t" %i, end="")
    iCount+=1; i+=1
if  iCount%7==1 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
if  iCount%7==2 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
if  iCount%7==3 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
if  iCount%7==4 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
if  iCount%7==5 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
if  iCount%7==6 and i<=days[month-1]:
    print ("%.2i\t" %i, end="")
