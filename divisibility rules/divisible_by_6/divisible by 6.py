def divisible_by_6():
    num=input("Enter num : ")
    t=0
    for i in num:
        t+=int(i)
    if t % 3==0 and int(num) % 2==0:
        answer=int(num)//6
        print(f"{num} divisible by 6 the answer is {answer}")
    else:
        print(f"{num} not divisible by 6")
if __name__ == "__main__":
    divisible_by_6()
