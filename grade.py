#A teacher in a school wants to find and display the grade of a student based on his/her percentage score.
#The criterion for grades is as given below:
            #Score (both inclusive)	Grade
              #Between 80 and 100	    A
              #Between 73 and 79	    B
              #Between 65 and 72	    C
              #Between 0 and 64	      D
              #Any other value	      Z
              
              
              
score=50
if(score>=80 and score<=90):
    print("A")
elif(score>=70 and score<=79):
    print("B")
elif(score>=65 and score<=72):
    print("C")
elif(score>=0 and score<=64):
    print("D")
else:
    print("Z")
