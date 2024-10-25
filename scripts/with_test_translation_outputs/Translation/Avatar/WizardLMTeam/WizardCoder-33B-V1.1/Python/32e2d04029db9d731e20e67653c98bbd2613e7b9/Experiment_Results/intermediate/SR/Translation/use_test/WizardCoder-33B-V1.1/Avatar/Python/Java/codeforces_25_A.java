<｜begin▁of▁sentence｜>Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
20
88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46

Expected output:
4


```
n = int ( input ( ) )
list = [ int ( x ) % 2 for x in input ( ).split ( ) ]
if sum ( list ) == 1 :
    print ( list.index ( 1 ) + 1 )
else :
    print ( list.index ( 0 ) + 1 )


```

### Response:
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] list = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = scanner.nextInt() % 2;
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += list[i];
        }
        if (sum == 1) {
            for (int i = 0; i < n; i++) {
                if (list[i] == 1) {
                    System.out.println(i + 1);
                    break;
                }
            }
        } else {
            for (int i = 0; i < n; i++) {
                if (list[i] == 0) {
                    System.out.println(i + 1);
                    break;
                }
            }
        }
    }
}
```

This Java code does the same thing as the Python code. It reads an integer n from the standard input, then reads n integers from the standard input, applies the modulo 2 operation to each of them, and stores the results in an array. It then calculates the sum of all elements in the array. If the sum is 1, it prints the index of the first 1 in the array plus 1. If the sum is not 1, it prints the index of the first 0 in the array plus 1. <｜end▁of▁sentence｜>