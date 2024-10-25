<s> [INST] <<SYS>>
You are an expert Java programmer and assistant
<</SYS>>

Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
7
1 1
2 1
3 1
4 1
5 1
6 1
7 1

Expected output:
3


```
n = int ( input ( ) )
l = [ 0 for _ in range ( 1000010 ) ]
dp = [ 0 for _ in range ( 1000010 ) ]
for i in range ( n ) :
    a , b = map ( int , input ( ).split ( ) )
    l [ a ] = b
if l [ 0 ] > 0 :
    dp [ 0 ] = 1
mx = 0
for i in range ( 1 , 1000010 ) :
    if ( l [ i ] == 0 ) :
        dp [ i ] = dp [ i - 1 ]
    else :
        if ( l [ i ] >= i ) :
            dp [ i ] = 1 ;
        else :
            dp [ i ] = dp [ i - l [ i ] - 1 ] + 1 ;
    if ( dp [ i ] > mx ) :
        mx = dp [ i ]
print ( n - mx )


```
[/INST]
```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] l = new int[1000010];
        int[] dp = new int[1000010];

        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            l[a] = b;
        }

        if (l[0] > 0) {
            dp[0] = 1;
        }

        int mx = 0;
        for (int i = 1; i < 1000010; i++) {
            if (l[i] == 0) {
                dp[i] = dp[i - 1];
            } else {
                if (l[i] >= i) {
                    dp[i] = 1;
                } else {
                    dp[i] = dp[i - l[i] - 1] + 1;
                }
            }
            if (dp[i] > mx) {
                mx = dp[i];
            }
        }

        System.out.println(n - mx);
    }
}
```
Note: The above code is a direct translation of the given Python code to Java. However, it is not the most efficient or elegant solution, and there may be better ways to solve the problem in Java.</s>
