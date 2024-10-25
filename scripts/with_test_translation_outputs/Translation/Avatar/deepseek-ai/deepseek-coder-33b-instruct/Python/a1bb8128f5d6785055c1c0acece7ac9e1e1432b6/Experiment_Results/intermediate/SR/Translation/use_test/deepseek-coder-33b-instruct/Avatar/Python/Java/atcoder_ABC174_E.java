<｜begin▁of▁sentence｜>You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
1 4784
450968417

Expected output:
94247


```
def check ( lis , k , mid ) :
    for i in lis :
        if ( i % mid == 0 ) :
            k += 1
        k -= ( i // mid )
    return k >= 0
n , k = map ( int , input ( ).split ( ) )
lis = list ( map ( int , input ( ).split ( ) ) )
a , b = 1 , max ( lis )
ans = b
while ( a <= b ) :
    mid = ( a + b ) // 2
    if ( check ( lis , k , mid ) ) :
        ans = mid
        b = mid - 1
    else :
        a = mid + 1
print ( ans )


```

### Response:
```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int[] lis = new int[n];
        for (int i = 0; i < n; i++) {
            lis[i] = scanner.nextInt();
        }
        int a = 1;
        int b = Arrays.stream(lis).max().getAsInt();
        int ans = b;
        while (a <= b) {
            int mid = (a + b) / 2;
            if (check(lis, k, mid)) {
                ans = mid;
                b = mid - 1;
            } else {
                a = mid + 1;
            }
        }
        System.out.println(ans);
    }

    public static boolean check(int[] lis, int k, int mid) {
        for (int i : lis) {
            if (i % mid == 0) {
                k++;
            }
            k -= (i / mid);
        }
        return k >= 0;
    }
}
```
<|EOT|>
