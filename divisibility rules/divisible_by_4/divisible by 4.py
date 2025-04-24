def divisible_by_4():
    num=input("Enter num : ")
    t=int(num[-2:])
    if t % 4==0:
        answer=int(num)//4
        print(f"{num} divisible by 4 ,the answer is {answer}")
    else:
        print(f"{num} not divisible by 4")
if __name__ == "__main__":
    divisible_by_4()
    
