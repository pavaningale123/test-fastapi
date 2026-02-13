# def reverse_string(s):
#     reverser_string=''
#     for i in range(len(s)-1,-1,-1):
#         reverser_string+=s[i]
#     return reverser_string

number=list(map(int,input("enter the no. sepated by space")
                .split()))
last_number=number[-1]
nest_number=last_number+1
print(nest_number)