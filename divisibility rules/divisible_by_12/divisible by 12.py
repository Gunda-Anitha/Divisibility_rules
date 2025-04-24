def divisible_by_12():
    num=input("Enter num : ")
    t1=0
    t2=int(num[-2:])
    for i in num:
        t1+=int(i)
    if t1 % 3==0 and t2 % 4 == 0:
        answer=int(num)//12
        print(f"{num} divisible by 12 the answer is {answer}")
    else:
        print(f"{num} not divisible by 12")
if __name__ == "__main__":
    divisible_by_12()