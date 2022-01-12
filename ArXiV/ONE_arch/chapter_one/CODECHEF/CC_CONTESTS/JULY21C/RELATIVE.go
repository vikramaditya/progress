/*
Author: valisport
Date: Friday 02 July 2021 06:22:49 PM IST
*/

package main

import "fmt"

func main() {
  var T int;
  fmt.Scanln(&T)

  for i:= T; i > 0; i--{
    var g,c,res int
    fmt.Scanln(&g, &c)
    res = (c*c) / (2*g)
    fmt.Println(res)
  }
}
