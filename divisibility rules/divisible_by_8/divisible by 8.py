def divisible_by_8():
    num=input("Enter num : ")
    t=int(num[-3:])
    if t % 8==0:
        answer=int(num)//8
        print(f"{num} divisible by 8, the answer is {answer}")
    else:
        print(f"{num} not divisible by 8")
if __name__ == "__main__":
    divisible_by_8()
    
