from math import sqrt
print("pythagroean theroem calculator ! calculate your traingle side:-")
print("assume the sides are a,b,c where c is the hypotenuse")
formulla=input("which side (a,b,c) do you wish to calulate")
if formulla=='c':
    side_a=int(input("enter the length of side a:-"))
    side_b=int(input("enter the length of side b:-"))
    side_c=sqrt(side_a*side_a+side_b*side_b)
    print("the length of side_c is:",side_c)
elif formulla=="a":
    side_b=int(input("enter the length of b:-"))
    side_c=int(input("enter the length of c:-"))
    side_a=sqrt((side_c*side_c)-(side_b*side_b))
    print("the length of side a is :-",side_a)
elif formulla=="b":
    side_a=int(input("enter the length of side a:-"))
    side_c=int(input("enter the length of the side c:-"))
    side_b=sqrt((side_c*side_c)-(side_a*side_a))
    print("the length of side_b is: ",side_b)
else:
    print('please select a side between a,b,c')
    
