/*
Author: valisport
Date: Friday 03 September 2021 03:00:46 PM IST
*/

package main
import "fmt"

func main(){
  var T, A, B, C, D, E, i int;
  fmt.Scanln(&T)

  for i = T; i > 0; i-- {
    fmt.Scanln(&A, &B, &C, &D, &E)
    if ( (A + B <= D && C <= E) || (A + C <= D && B <= E) || (B + C <= D && A <= E) ) {
      fmt.Println("YES")
    } else{
      fmt.Println("NO")
    }
  }
}

