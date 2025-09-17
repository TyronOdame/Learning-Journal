package main

import "fmt"
// this is an example of a global variable
var ex string = "Global string Example"





func adding(a int, b int) {
	fmt.Println(a + b)
}

func main() {
	name := "tyron"

	fmt.Println("Hello, Go Playground!")
	fmt.Println(name)
	adding(5, 10)
}