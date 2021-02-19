1height = float(input("請輸入你的身高cm")) 
weight = float(input("請輸入你的重量kg"))

height=height/100

BMI=weight/(height*height)

if BMI < 18.5:
   print("體重過輕")
   
if BMI >= 18.5 and BMI < 24:
   print("體重正常")

if BMI > 24 and BMI < 27:
   print("體重過重")

if BMI >= 27:
   print("肥胖")



