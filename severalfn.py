class multiplefunctions():

    def subfields():
        ITEMS=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Lnaguage Processing"]
        print("Subfields in AI are:")
        for fields in ITEMS:
            print(fields)

    def oddEven():
        num=int(input("Enter the number"))
        if(num%2==0):
            print(num,"is Even Number",)
            message=num,"is Even Nunber"
        else:
            print(num," is Odd Number",)
            message="is Odd Number"
        return message
        
    def eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if( gender=="Male"and age>=21):
            print("ELIGIBLE")
            message="ELIGIBLE"
        elif(gender=="Female" and age>=18):
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        return message
        
    def percentage():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        Total=subject1+subject2+subject3+subject4+subject5
        print("Total=",Total)
        max=500
        percentage=(Total/max*100)
        print("Percentage=",percentage)
        
    def triangle():
        height=int(input("Height"))
        breadth=int(input("Breadth"))
        print("Area Formula:(Height*Breadth)/2")
        Area=(height*breadth)/2
        print("Area of Triangle:",Area)
        message="Area of Triangle",Area
        height1=int(input("Height1"))
        height2=int(input("Height2"))
        breadth=int(input("Breadth"))
        print("perimeter formula:height1+height2+breadth")
        perimeter=height1+height2+breadth
        print("Perimeter of Triangle",perimeter)
        message="perimeter of triangle",perimeter
        return message