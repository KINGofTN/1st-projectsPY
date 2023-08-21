from hbd18 import rub as r 
print("-----------------------------------------")
print("|              [RK's] calculater        |")
print("-----------------------------------------")

select ="        .-choices the any operators-.     "

in1=int(input("1.enter the first number ?: "     ))
in2=int(input("2.enter the second number : "     ))
print("")
print(select)
print("""   
             1. addition       (+)
             2. subfraction    (-)
             3. multiplication (*)
             4. division       (/)
""")
in3=int(input("         enter the options number : "))
print("")
print("")

if in3 == 1:
    a=in1+in2
    print("               TOTAL VALUE :"+""+str(a))
elif in3 == 2:
    b=in1-in2
    print("               TOTAL VALUE :"+""+str(b))
elif in3 == 3:
    c=in1*in2
    print("               TOTAL VALUE :"+""+str(c))
elif in3 == 4:
    d=in1//in2
    print("               TOTAL VALUE :"+""+str(d)) 
else:
    e="           invalid options numbers"
    print(e)   
    
print("-------------------------------------------") 
print("            .-THANKS FOR USE ME-.         ")
print("-------------------------------------------") 
print()
r()