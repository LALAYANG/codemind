<｜begin▁of▁sentence｜>You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
1111111111111111111

Expected output:
162261460


```
mod = 10 ** 9 + 7
l = input ( )
n = len ( l )
dp = [ [ 0 ] * 2 for _ in range ( n + 1 ) ]
dp [ 0 ] [ 0 ] = 1
for i , c in enumerate ( l ) :
    if c == '0' :
        dp [ i + 1 ] [ 0 ] += dp [ i ] [ 0 ]
        dp [ i + 1 ] [ 1 ] += dp [ i ] [ 1 ] * 3
    else :
        dp [ i + 1 ] [ 0 ] += dp [ i ] [ 0 ] * 2
        dp [ i + 1 ] [ 1 ] += dp [ i ] [ 0 ]
        dp [ i + 1 ] [ 1 ] += dp [ i ] [ 1 ] * 3
    dp [ i + 1 ] [ 0 ] %= mod
    dp [ i + 1 ] [ 1 ] %= mod
print ( ( dp [ n ] [ 0 ] + dp [ n ] [ 1 ] ) % mod )


```

### Response:
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String l = scanner.nextLine();
        int n = l.length();
        long mod = (long)Math.pow(10, 9) + 7;
        long[][] dp = new long[n + 1][2];
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            char c = l.charAt(i);
            if (c == '0') {
                dp[i + 1][0] += dp[i][0];
                dp[i + 1][1] += dp[i][1] * 3;
            } else {
                dp[i + 1][0] += dp[i][0] * 2;
                dp[i + 1][1] += dp[i][0];
                dp[i + 1][1] += dp[i][1] * 3;
            }
            dp[i + 1][0] %= mod;
            dp[i + 1][1] %= mod;
        }
        System.out.println((dp[n][0] + dp[n][1]) % mod);
    }
}
```
<|EOT|>
