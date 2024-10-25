<s> [INST] <<SYS>>
You are an expert Java programmer and assistant
<</SYS>>

Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
5 4 11 80 2 4

Expected output:
YES


```
xxs = input ( ).split ( " " )
x , t , a , b , da , db = int ( xxs [ 0 ] ) , int ( xxs [ 1 ] ) , int ( xxs [ 2 ] ) , int ( xxs [ 3 ] ) , int ( xxs [ 4 ] ) , int ( xxs [ 5 ] )
def main ( ) :
    if x == 0 :
        print ( "YES" )
        return "Result Found"
    a_time = min ( [ a // da , t - 1 ] )
    b_time = min ( [ b // db , t - 1 ] )
    for i in range ( a_time + 1 ) :
        for j in range ( b_time + 1 ) :
            if a - da * i == x or b - db * j == x :
                print ( "YES" )
                return "Result Found"
            if ( a - da * i ) + ( b - db * j ) == x :
                print ( "YES" )
                return "Result Found"
    return "Result Not Found"
ff = main ( )
if ff == "Result Not Found" :
    print ( "NO" )


```
[/INST]
```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int t = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int da = sc.nextInt();
        int db = sc.nextInt();

        if (x == 0) {
            System.out.println("YES");
            return;
        }

        int aTime = Math.min(a / da, t - 1);
        int bTime = Math.min(b / db, t - 1);

        for (int i = 0; i <= aTime; i++) {
            for (int j = 0; j <= bTime; j++) {
                if (a - da * i == x || b - db * j == x) {
                    System.out.println("YES");
                    return;
                }
                if ((a - da * i) + (b - db * j) == x) {
                    System.out.println("YES");
                    return;
                }
            }
        }

        System.out.println("NO");
    }
}
```
Note: In the Java code, I have used the `Math.min()` method to find the minimum of two values, as it is not possible to use the `min()` function in Java like in Python.</s>
