
year=int(input("輸入年份："))
month = int(input("請輸入月："))


days=[31,28,31,30,31,30,31,31,30,31,30,31]

year1=year-1
totalDays=int(year1*365+year1/4+year1/400-year1/100);

if year%4==0:
      days[1]=29

for i in range(month-1):
    totalDays=totalDays+days[i]
print(days[1]) 
iCount = 0
print ("日\t一\t二\t三\t四\t五\t六")
for i in range(int(totalDays)%7+1):
    print ('\t', end=""),
    iCount+=1
for i in range(1,days[month-1]+1):
    print ("%.2i\t" %i, end=""),
    iCount +=1
    if iCount%7 == 0 :
      print ('')




