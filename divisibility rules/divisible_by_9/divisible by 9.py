def divisible_by_9():
    num=input("Enter num : ")
    t=0
    for i in num:
        t+=int(i)
    if t % 9==0:
        answer=int(num)//9
        print(f"{num} divisible by 9 the answer is {answer}")
    else:
        print(f"{num} not divisible by 9")
if __name__ == "__main__":
    divisible_by_9()
