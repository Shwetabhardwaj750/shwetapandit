#grade_students

score = int(input("enter your score:"))
if score>=90 and score<= 100:
    print("grade A")
elif score>=80 and score<90:
    print("gade B")
elif score>=70 and score<80:
    print("grade B")
elif score>=60 and score<70:
    print("grade C")
else:
    print("grade D")

#MORE CLEAR WAY
if 90<= score<=100:
    print("grade A")
elif 80>=score<90:
    print("grade B")
elif 70>=score<80:
    print("grade C")
elif 60>=score<70:
    print("grade D")
else :
    print("grade E")

