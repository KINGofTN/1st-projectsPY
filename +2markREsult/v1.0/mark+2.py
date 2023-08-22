#comparison opera ands "=="
# >,<,<=,>=
# or,and,not

#       school mark is project
tamil = int(input("1.enter your tamil mark is :")) 
english = int(input("2.enter your english mark is :"))
maths = int(input("3.enter your maths mark is :")) 
physics = int(input("4.enter your physics mark is :")) 
chemistry = int(input("5.enter your chemistry mark is :")) 
biology = int(input("6.enter your biology mark is:")) 
print("")
print("")
print("------------------------------------------")
print("                +2,RESULTS     hi         ")
print("------------------------------------------")
print("")
if tamil >=35 and tamil <=100:
    print("1.    tamil         -             pass ")  
if tamil > 100:
    print("tamil mark is over the 100")
if tamil <35:
    print("1.    tamil         -             fail ")
if english > 100:
    print("english mark is over the 100")         
if english >=35 and english <=100:
    print("2.   english        -             pass ")   
if english <35:
    print("2.   english        -             fail ")
if maths > 100:
    print("maths mark is over the 100")    
if maths >=35 and maths <=100:
    print("3.    maths         -             pass ")
if maths <35:
    print("3.    maths         -             fail ")
if physics > 100:
    print("physics mark is over the 100")    
if physics >=35 and physics <=100:
    print("4.    physics       -             pass ")    
if physics <35:
    print("4.    physics       -             fail ")
if chemistry > 100:
    print("chemistry mark is over the 100")       
if chemistry >=35 and chemistry <=100:
    print("5.   chemistry      -             pass ")        
if chemistry <35:
    print("5.   chemistry      -             fail ")
if biology > 100:
    print("biology mark is over the 100")       
if biology >=35 and biology <=100:
    print("6.    biology       -             pass ")
if biology <35:
    print("6.    biology       -             fail ")      
x=tamil+english+maths+chemistry+physics+biology   
print("              TOTAL :"+str(x))    




    

