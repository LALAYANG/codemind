<｜begin▁of▁sentence｜>You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
3 3
1 2
1 3
2 3

Expected output:
1

```
def readInts ( ) : return map ( int , input ( ).split ( ) )
def dfs ( g , seen , i ) :
    if i in seen :
        return 0 , 0
    seen.add ( i )
    nodes = 1
    edges = len ( g [ i ] )
    for j in g [ i ] :
        x , y = dfs ( g , seen , j )
        nodes += x
        edges += y
    return nodes , edges
def solve ( ) :
    line0 = [ ]
    try : line0 = readInts ( )
    except EOFError : return False
    n , m = line0
    g = { }
    seen = set ( )
    for i in range ( 1 , n + 1 ) :
        g [ i ] = set ( )
    for _ in range ( m ) :
        a , b = readInts ( )
        g [ a ].add ( b )
        g [ b ].add ( a )
    ans = 0
    for i in range ( 1 , n + 1 ) :
        if i not in seen :
            nodes , edges = dfs ( g , seen , i )
            if nodes > 1 and nodes % 2 == 1 and 2 * nodes == edges :
                ans += 1
    if ( n - ans ) % 2 == 1 :
        ans += 1
    print ( ans )
    return True
while solve ( ) : pass


```

### Response:
```java
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        while (solve()) ;
    }

    static int[] readInts() {
        String[] line = sc.nextLine().split(" ");
        int[] res = new int[line.length];
        for (int i = 0; i < line.length; i++) {
            res[i] = Integer.parseInt(line[i]);
        }
        return res;
    }

    static int[] dfs(Map<Integer, Set<Integer>> g, Set<Integer> seen, int i) {
        if (seen.contains(i)) {
            return new int[]{0, 0};
        }
        seen.add(i);
        int nodes = 1;
        int edges = g.get(i).size();
        for (int j : g.get(i)) {
            int[] xy = dfs(g, seen, j);
            nodes += xy[0];
            edges += xy[1];
        }
        return new int[]{nodes, edges};
    }

    static boolean solve() {
        int[] line0 = readInts();
        if (line0.length == 0) {
            return false;
        }
        int n = line0[0];
        int m = line0[1];
        Map<Integer, Set<Integer>> g = new HashMap<>();
        Set<Integer> seen = new HashSet<>();
        for (int i = 1; i <= n; i++) {
            g.put(i, new HashSet<>());
        }
        for (int i = 0; i < m; i++) {
            int[] ab = readInts();
            int a = ab[0];
            int b = ab[1];
            g.get(a).add(b);
            g.get(b).add(a);
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (!seen.contains(i)) {
                int[] nodesEdges = dfs(g, seen, i);
                int nodes = nodesEdges[0];
                int edges = nodesEdges[1];
                if (nodes > 1 && nodes % 2 == 1 && 2 * nodes == edges) {
                    ans += 1;
                }
            }
        }
        if ((n - ans) % 2 == 1) {
            ans += 1;
        }
        System.out.println(ans);
        return true;
    }
}
```
<|EOT|>