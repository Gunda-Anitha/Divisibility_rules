def divisible_by_10():
    num=input("Enter num : ")
    t=int(num[-1:])
    if t == 0:
        answer=int(num)//10
        print(f"{num} divisible by 10, the answer is {answer}")
    else:
        print(f"{num} not divisible by 10")
if __name__ == "__main__":
    divisible_by_10()
    
