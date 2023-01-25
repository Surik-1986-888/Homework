#  

# str1='karavarutyun'  
# x=dict(map(lambda y:(y,str1.count(y)),str1))
# print(x)


# def my_funktion():
#  while True:
#     paasss=input("enter_your_passvord_")
#     dig=0
#     upprr=0
#     if len(paasss)>=8:
#     for i in paasss:
#         if i.isdigit():
#             dig=+1
#             elif i.isupper():
#                upprr=+1 
#                if upper>=1 and dig>=1
#                print("strong passford")
#                break

#           else:
#           print("tray again")  
#    my_funktion() 




list1=['@','!','%','*','&']
def pass_kass():
    while True:
        count_upper=0
        count_digit=0
        count_symbol=0
        count_prabel=0
        passeord=input("Enter_your_passvord_")
        if len(passeord)<8:
            print('your_pasvord_short')
            continue
        else:
            for i in passeord:
                if i.isupper():
                    count_upper+=1
                elif i.isdigit():
                    count_digit+=1
                elif i in list1:
                    count_symbol+=1
                elif i == ' ':
                  count_prabel+=1
        if count_upper>=2 and count_digit>=2 and count_symbol>=1 and count_prabel>=2:
            print('your_password_is_safety')
            break
        else:
            print('your_password_isnot_safety') 
pass_kass()
            
