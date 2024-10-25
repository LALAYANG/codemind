<s> [INST] <<SYS>>
You are an expert Java programmer and assistant
<</SYS>>

Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
3 5
1 2 3
1 1 1 1 1

Expected output:
2


```
def main ( ) :
    n , m = [ int ( i ) for i in input ( ).split ( ) ]
    round_complexity = [ int ( i ) for i in input ( ).split ( ) ]
    george_complexity = [ int ( i ) for i in input ( ).split ( ) ]
    i = j = 0
    while ( i < n and j < m ) :
        i += 1 * ( round_complexity [ i ] <= george_complexity [ j ] ) ;
        j += 1
    print ( n - i )
if __name__ == '__main__' :
    main ( )


```
[/INST]
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[] roundComplexity = new int[n];
        int[] georgeComplexity = new int[m];
        for (int i = 0; i < n; i++) {
            roundComplexity[i] = scanner.nextInt();
        }
        for (int i = 0; i < m; i++) {
            georgeComplexity[i] = scanner.nextInt();
        }
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (roundComplexity[i] <= georgeComplexity[j]) {
                i++;
            }
            j++;
        }
        System.out.println(n - i);
    }
}
```
Note: The above code is a direct translation of the given Python code to Java. However, it is not the most efficient or elegant solution to the problem. A more efficient solution would involve using a more appropriate data structure, such as a priority queue, to keep track of the round and George's complexity.</s>
