<｜begin▁of▁sentence｜>You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
10 40
5 4 3 2 -1 0 0 0 0 0

Expected output:
6


```
N , K = map ( int , input ( ).split ( ) )
A = list ( map ( int , input ( ).split ( ) ) )
A.sort ( )
ll = - 10 ** 18 - 1
rr = 10 ** 18 + 1
while ll + 1 < rr :
    x = ( ll + rr ) // 2
    tot = 0
    for i in range ( N ) :
        if A [ i ] < 0 :
            l = - 1
            r = N
            while l + 1 < r :
                c = ( l + r ) // 2
                if A [ i ] * A [ c ] < x :
                    r = c
                else :
                    l = c
            tot += N - r
        else :
            l = - 1
            r = N
            while l + 1 < r :
                c = ( l + r ) // 2
                if A [ i ] * A [ c ] < x :
                    l = c
                else :
                    r = c
            tot += r
        if A [ i ] * A [ i ] < x :
            tot -= 1
    tot //= 2
    if tot < K :
        ll = x
    else :
        rr = x
print ( ll )


```

### Response:
```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        Arrays.sort(A);
        long ll = -(long)1e18 - 1;
        long rr = (long)1e18 + 1;
        while (ll + 1 < rr) {
            long x = (ll + rr) / 2;
            long tot = 0;
            for (int i = 0; i < N; i++) {
                if (A[i] < 0) {
                    int l = -1;
                    int r = N;
                    while (l + 1 < r) {
                        int c = (l + r) / 2;
                        if ((long)A[i] * A[c] < x) {
                            r = c;
                        } else {
                            l = c;
                        }
                    }
                    tot += N - r;
                } else {
                    int l = -1;
                    int r = N;
                    while (l + 1 < r) {
                        int c = (l + r) / 2;
                        if ((long)A[i] * A[c] < x) {
                            l = c;
                        } else {
                            r = c;
                        }
                    }
                    tot += r;
                }
                if ((long)A[i] * A[i] < x) {
                    tot--;
                }
            }
            tot /= 2;
            if (tot < K) {
                ll = x;
            } else {
                rr = x;
            }
        }
        System.out.println(ll);
    }
}
```
<|EOT|>