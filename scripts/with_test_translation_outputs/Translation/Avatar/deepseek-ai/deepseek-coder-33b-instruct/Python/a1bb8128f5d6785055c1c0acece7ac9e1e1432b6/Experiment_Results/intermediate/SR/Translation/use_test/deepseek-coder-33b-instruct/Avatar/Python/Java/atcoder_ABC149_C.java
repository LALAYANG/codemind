<｜begin▁of▁sentence｜>You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
56588

Expected output:
56591


```
X = int ( input ( ) )
prime = [ True ] * ( 100010 )
prime [ 0 ] = False ;
prime [ 1 ] = False ;
for i in range ( 4 , 100010 , 2 ) :
    prime [ i ] = False
i = 3
while ( i * i <= 100008 ) :
    if prime [ i ] :
        for j in range ( i + i , 100008 , i ) :
            prime [ j ] = False
    i += 2
for i in range ( X , 100008 ) :
    if prime [ i ] :
        print ( i )
        break


```

### Response:
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        boolean[] prime = new boolean[100010];
        for (int i = 0; i < 100010; i++) {
            prime[i] = true;
        }
        prime[0] = false;
        prime[1] = false;
        for (int i = 4; i < 100010; i += 2) {
            prime[i] = false;
        }
        int i = 3;
        while (i * i <= 100008) {
            if (prime[i]) {
                for (int j = i + i; j < 100008; j += i) {
                    prime[j] = false;
                }
            }
            i += 2;
        }
        for (int j = X; j < 100008; j++) {
            if (prime[j]) {
                System.out.println(j);
                break;
            }
        }
    }
}
```
<|EOT|>