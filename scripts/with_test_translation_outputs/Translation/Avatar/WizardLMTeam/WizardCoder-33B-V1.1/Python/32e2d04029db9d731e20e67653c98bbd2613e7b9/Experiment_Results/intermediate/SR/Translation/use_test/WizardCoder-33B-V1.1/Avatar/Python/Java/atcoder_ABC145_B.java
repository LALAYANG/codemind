<｜begin▁of▁sentence｜>Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
94
zrimlvumuarenexcfycebfurgvjyospdhvuyfvtvnrdyluazrimlvumuarenexcfycebeurgvjyospdhvuyfvtvnrdylua

Expected output:
No


```
n = int ( input ( ) )
s = input ( )
if n % 2 != 0 : print ( 'No' )
elif s [ : int ( n / 2 ) ] == s [ int ( n / 2 ) : ] : print ( 'Yes' )
else : print ( 'No' )


```

### Response:
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String s = scanner.next();
        if (n % 2 != 0) {
            System.out.println("No");
        } else if (s.substring(0, n / 2).equals(s.substring(n / 2, n))) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
```

Test input:
94
zrimlvumuarenexcfycebfurgvjyospdhvuyfvtvnrdyluazrimlvumuarenexcfycebeurgvjyospdhvuyfvtvnrdylua

Expected output:
No <｜end▁of▁sentence｜>
