'''Problem Statement:

Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.

'''

#note : the indentation should keep in mind (here I haven't checked the indentation)

def find_product(num1,num2,num3):
    product=0
    #write your logic here

	#case 1: first number only is 7
    if(num1==7 and num2!=7 and num3!=7):
	product =num2*num3
	
	#case 2: second number only is 7
    elif(num2==7 and num3!=7):
	product =num3

	#case 3: third number alone is 7
    elif(num3==7):
	product = -1

	#case 4: first and second number is 7
    elif(num1==7 and num2==7 and num3!=7):
	product=num3

	#case 5: 3 numbers are not 7 	
    else:
	 product =num1 *num2*num3;


    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)
