def divisible_by_3():
    num=input("Enter num : ")
    t=0
    for i in num:
        t+=int(i)
    if t % 3==0:
        answer=int(num)//3
        print(f"{num} divisible by 3 the answer is {answer}")
    else:
        print(f"{num} not divisible by 3")
if __name__ == "__main__":
    divisible_by_3()