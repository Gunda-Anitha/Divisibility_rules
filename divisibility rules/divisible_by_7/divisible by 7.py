def divisible_by_7():
    num=input("Enter num : ")
    l=int(num[-1:])
    t=int(num[0:-1])-(2*l)
    if t % 7==0:
        answer=int(num)//7
        print(f"{num} divisible by 7, the answer is {answer}")
    else:
        print(f"{num} not divisible by 7")
if __name__ == "__main__":
    divisible_by_7()
    
