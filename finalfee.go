//Write a Go program to calculate and display the final fees to be paid by a student.

//The students are entitled to get scholarship based on the marks scored in the qualifying exam. Scholarship percentage should be considered as half of the marks scored by the student on the course fee. Apart from the course fee (after deducting the scholarship amount), the students have to pay an extra service fees.

//Consider that course fee, marks scored by the student and extra fees amount are given. Assume that the marks is out of 100 and need not always be integer

//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee float32
    //Write your program logic here
    //Populate the variable: finalFee
    var course_fee float32=25000
    var extra_fee float32=1500
    var marks float32=50
    var percentage float32=(marks/2)/100
    var scholarship_amount float32= percentage*course_fee
    finalFee=course_fee-scholarship_amount+extra_fee
     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
