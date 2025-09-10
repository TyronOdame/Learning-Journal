# Intro to GO

For starters, when you want to 'build' a Go file, you need to run the following command in the terminal

```bash
go build main.go
```

**Note that** _building_ a files create a version of the file that is essentially complied into executable binary code. Creating a output file with the default name given to the file

if done correctly, when you run the `ls` command in your terminal, you should see

```bash
main       main.go
```

running the new complied file is easy with the `./main` command.

However, if you are not quite ready to commit and compile the file but want to see what the outcome will be, you can run the following code in the terminal

```bash
go run main.go
```

this will allow you to see all the current changes that you've made on a file to track what's been done already

## Starting a file

One of the first things that you want to do when you start a GO file is import packages

without these packages or libraries, you won't have access to other functionalities that you would need to build your application. In other words you would be limited to just the default functions that GO comes with

the first main package will be main

```go
package main
```

within the main library, you have access to _fmt_, which is a import you would make to have the ability to make outputs and things of that nature

```go
package main

import "fmt"
```

you can also import more then once in a file

```go
import "fmt"
import "math"
import "time"
```

Or you can do it this way

```go
import (
    "fmt"
    "math"
    "time"
)
```

After we created our imports, its time to create our first function. Here is what the syntax looks like

```go
func main () {
    fmt.Println("Hello, World")
}
```

_func_ is the keyword that you will use when creating functions in GO. This is the only way to declare functions so do not forget

## Variables

There are a couple of ways that variables can be made. One way is to just declare them like so.

```Go
var exampleVar string
```

With this way, you are creating the variable and stating what type of value it will be taking

```go
var exampleVar string = "Hello World"
```

This one is the same as the first example, except that you are also setting the variable to be equal to a value (that matches the stated data Type)

```go
var exampleVar = "Hello World"
```

This looks like it is the same as the previous example. However, the data type is not specified. This is called a _inferred variable_ ( not actually sure what its called but the data type is inferred by the data it is set to )

```go
var exampleVar := "seven"
```

Last but not least is the short handed way of creating a variable. This is also a inferred variable where I am declaring and setting the variable to a value
