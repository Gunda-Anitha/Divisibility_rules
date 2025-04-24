def divisible_by_11():
    num=input("Enter num : ")
    even=[]
    odd=[]
    for i in range(len(num)):
        if i % 2==0:
            even.append(int(num[i]))
        else:
            odd.append(int(num[i]))
    t=sum(even)-sum(odd)
    if t %11 == 0:
        answer=int(num)//11
        print(f"{num} divisible by 11, the answer is {answer}")
    else:
        print(f"{num} not divisible by 11")
if __name__ == "__main__":
    divisible_by_11()
    
