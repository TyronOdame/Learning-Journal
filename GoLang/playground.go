package main

import "fmt"
// this is an example of a global variable
var ex string = "Global string Example"

var num int = 12
var num2 int = 15


func addingNums() {
	fmt.Println(num + num2)
	if num + num2 > 20 {
		fmt.Println("Greater than 20")
	} else {
		fmt.Println("Less than 20")
	}
}

func adding(a int, b int) {
	fmt.Println(a + b)
}

func main() {
	name := "tyron"

	fmt.Println("Hello, Go Playground!")
	fmt.Println(name)
	adding(5, 10)
	addingNums()
}