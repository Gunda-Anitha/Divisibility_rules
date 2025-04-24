def divisible_by_5():
    num=input("Enter num : ")
    t=int(num[-1:])
    if t % 5==0:
        answer=int(num)//5
        print(f"{num} divisible by 5, the answer is {answer}")
    else:
        print(f"{num} not divisible by 5")
if __name__ == "__main__":
    divisible_by_5()
    
