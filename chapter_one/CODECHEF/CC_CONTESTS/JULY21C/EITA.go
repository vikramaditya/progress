/*
Author: valisport
Date: Friday 02 July 2021 05:34:52 PM IST
*/

package main

import "fmt"

func main() {
  var T,d,x,y,z int

  fmt.Scanln(&T)

  for i := T ; i > 0; i-- {
    fmt.Scanln(&d, &x, &y, &z)

    var str_one int
    str_one = x * 7

    var str_two int

    for j := d; j > 0; j-- {
      str_two += y
    }

    var rem int
    rem = 7 - d

    for j := rem; j > 0; j-- {
      str_two += z
    }

    if str_one > str_two {
      fmt.Println(str_one)
    } else {
      fmt.Println(str_two)
    }
  }
}

