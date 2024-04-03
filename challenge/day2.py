# n = int(input())
def facto(f):
    prod = 1
    for i  in range(1,f+1):
        prod = prod * i
    return prod
# int(facto(n))

rep = int(input())
fact = []
for i in range(rep):
    value = int(input())
    fact.append(facto(value))
for i in range(len(fact)):
    fact[i] = fact[i]%10
    # if(len(fact[i])>2):
    # print(fact[i][-1])
    # else:
    print(fact[i])
    
    
    
    
# prod = 1
# liste =[] 
# while prod <= facto(val):
#     if prod == facto(val):
#         for i in range(len(liste)-1):
#             print(liste[i])
#         print(facto(val))
#         break   
    
#     val_enter = int(input())
#     liste.append(val_enter)
#     prod *= val_enter 
    
#     if prod >= facto(val):
#         continue
        
# else:  
#     n = input()
#     print("O")
#     print(facto(val))      

#     if(prod>facto(val)):
#         print("0")
#         print(facto(val))
# if(prod == facto(val)):
#     print("cest bon")
 


# a=[];
# for i in range(4):
#     a.append(0)

# a[0] = input('');a[1] = input('');a[2] = input(''); a[3] = input('')
# for  i in range(len(a)):
#     if(a[i]==''):
#         a[i]=0
#     a[i] = int(a[i])
# prod = 1
# for i in range(1, len(a)):
#     prod = prod * a[i]
#     if(a[i] == 0):
#         print("0")
    #     print(a[0])
    #     break
    # if(i!=len(a)-1):
    #     print(a[i])
    # else:
    #     print(prod)

    