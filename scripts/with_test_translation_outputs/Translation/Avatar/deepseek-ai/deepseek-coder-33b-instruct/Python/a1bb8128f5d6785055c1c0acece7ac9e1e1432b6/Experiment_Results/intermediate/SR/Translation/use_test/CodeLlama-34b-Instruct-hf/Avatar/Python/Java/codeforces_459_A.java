<s> [INST] <<SYS>>
You are an expert Java programmer and assistant
<</SYS>>

Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
-100 -100 -100 100

Expected output:
100 -100 100 100


```
import math
given = input ( "" )
l1 = given.split ( )
l1 = [ int ( x ) for x in l1 ]
x1 = l1 [ 0 ]
y1 = l1 [ 1 ]
x2 = l1 [ 2 ]
y2 = l1 [ 3 ]
denominator = x2 - x1
numerator = y2 - y1
if denominator != 0 :
    quotient = numerator / denominator
if numerator == 0 :
    d = int ( math.sqrt ( ( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2 ) )
    x4 = x1
    x3 = x2
    y3 = y2 + d
    y4 = y1 + d
    print ( f"{x3} {y3} {x4} {y4}" )
elif denominator == 0 :
    y4 = y2
    y3 = y1
    d = int ( math.sqrt ( ( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2 ) )
    x4 = x1 + d
    x3 = x2 + d
    print ( f"{x3} {y3} {x4} {y4}" )
elif quotient == 1 :
    x4 = x2
    x3 = x1
    y4 = y1
    y3 = y2
    print ( f"{x3} {y3} {x4} {y4}" )
elif quotient == - 1 :
    x4 = x1
    x3 = x2
    y4 = y2
    y3 = y1
    print ( f"{x3} {y3} {x4} {y4}" )
else :
    print ( '-1' )


```
[/INST]
```java
import java.util.Scanner;

public class Quotient {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();

        int denominator = x2 - x1;
        int numerator = y2 - y1;

        if (denominator != 0) {
            int quotient = numerator / denominator;
            if (quotient == 1) {
                int x4 = x2;
                int x3 = x1;
                int y4 = y1;
                int y3 = y2;
                System.out.println(x3 + " " + y3 + " " + x4 + " " + y4);
            } else if (quotient == -1) {
                int x4 = x1;
                int x3 = x2;
                int y4 = y2;
                int y3 = y1;
                System.out.println(x3 + " " + y3 + " " + x4 + " " + y4);
            } else {
                System.out.println("-1");
            }
        } else {
            int d = (int) Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
            int x4 = x1 + d;
            int x3 = x2 + d;
            int y3 = y2 + d;
            int y4 = y1 + d;
            System.out.println(x3 + " " + y3 + " " + x4 + " " + y4);
        }
    }
}
```
Note: In the Java code, I have used `Math.sqrt` to calculate the square root of the sum of the squares of the differences between the x and y coordinates. This is equivalent to the Python code `math.sqrt((x2-x1)**2 + (y2-y1)**2)`.</s>
