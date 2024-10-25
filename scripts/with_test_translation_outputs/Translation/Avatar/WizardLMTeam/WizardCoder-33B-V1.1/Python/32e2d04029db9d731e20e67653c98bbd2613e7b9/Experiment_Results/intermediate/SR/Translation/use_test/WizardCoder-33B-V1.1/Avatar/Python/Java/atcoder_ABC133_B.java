<｜begin▁of▁sentence｜>Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3

Expected output:
2


```
import math
n , d = map ( int , input ( ).split ( ) )
points = [ list ( map ( int , input ( ).split ( ) ) ) for _ in range ( n ) ]
def dist ( x , y ) :
    tmp = 0.0
    for i in range ( d ) :
        tmp += ( x [ i ] - y [ i ] ) ** 2
    return math.sqrt ( tmp )
count = 0
for i , elm in enumerate ( points ) :
    for j in range ( i + 1 , n ) :
        if dist ( elm , points [ j ] ).is_integer ( ) :
            count += 1
print ( count )


```

### Response:
```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();
        int[][] points = new int[n][d];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < d; j++) {
                points[i][j] = scanner.nextInt();
            }
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isInteger(dist(points[i], points[j]))) {
                    count++;
                }
            }
        }
        System.out.println(count);
    }

    private static double dist(int[] x, int[] y) {
        double tmp = 0.0;
        for (int i = 0; i < x.length; i++) {
            tmp += Math.pow(x[i] - y[i], 2);
        }
        return Math.sqrt(tmp);
    }

    private static boolean isInteger(double num) {
        return num == Math.floor(num);
    }
}
```

This Java code does the same thing as the Python code. It reads the number of points and the dimension of the points from the standard input, then reads the points themselves. It calculates the Euclidean distance between each pair of points and checks if the distance is an integer. If it is, it increments a counter. Finally, it prints the counter. <｜end▁of▁sentence｜>