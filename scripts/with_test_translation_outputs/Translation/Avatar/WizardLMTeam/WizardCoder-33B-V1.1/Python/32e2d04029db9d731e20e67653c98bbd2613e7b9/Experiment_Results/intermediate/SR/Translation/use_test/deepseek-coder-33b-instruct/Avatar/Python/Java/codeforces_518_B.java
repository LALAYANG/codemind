<｜begin▁of▁sentence｜>You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.

### Instruction:
Translate the following Python code to Java and enclose your solution inside ```java and ```.
A sample test case is provided below:

Test input:
ncMeXssLHS
uwyeMcaFatpInZVdEYpwJQSnVxLK

Expected output:
6 1


```
s , t = input ( ) , input ( )
freqs = dict ( )
freqt = dict ( )
yay , whoops = 0 , 0
for letra in s :
    if letra in freqs :
        freqs [ letra ] += 1
    else :
        freqs [ letra ] = 1
for letra in t :
    if letra in freqt :
        freqt [ letra ] += 1
    else :
        freqt [ letra ] = 1
for letra in freqs.keys ( ) :
    while ( freqs [ letra ] > 0 and letra in freqt and freqt [ letra ] > 0 ) :
        yay += 1
        freqs [ letra ] -= 1
        freqt [ letra ] -= 1
for letra in freqs.keys ( ) :
    while ( freqs [ letra ] > 0 ) :
        if letra.islower ( ) and letra.upper ( ) in freqt.keys ( ) and freqt [ letra.upper ( ) ] > 0 :
            whoops += 1
            freqs [ letra ] -= 1
            freqt [ letra.upper ( ) ] -= 1
        elif letra.isupper ( ) and letra.lower ( ) in freqt.keys ( ) and freqt [ letra.lower ( ) ] > 0 :
            whoops += 1
            freqs [ letra ] -= 1
            freqt [ letra.lower ( ) ] -= 1
        else :
            break ;
print ( yay , whoops )


```

### Response:
Here is the Java version of the Python code:

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        String t = scanner.next();
        Map<Character, Integer> freqs = new HashMap<>();
        Map<Character, Integer> freqt = new HashMap<>();
        int yay = 0, whoops = 0;
        for (char letra : s.toCharArray()) {
            freqs.put(letra, freqs.getOrDefault(letra, 0) + 1);
        }
        for (char letra : t.toCharArray()) {
            freqt.put(letra, freqt.getOrDefault(letra, 0) + 1);
        }
        for (char letra : freqs.keySet()) {
            while (freqs.get(letra) > 0 && freqt.containsKey(letra) && freqt.get(letra) > 0) {
                yay++;
                freqs.put(letra, freqs.get(letra) - 1);
                freqt.put(letra, freqt.get(letra) - 1);
            }
        }
        for (char letra : freqs.keySet()) {
            while (freqs.get(letra) > 0) {
                if (Character.isLowerCase(letra) && freqt.containsKey(Character.toUpperCase(letra)) && freqt.get(Character.toUpperCase(letra)) > 0) {
                    whoops++;
                    freqs.put(letra, freqs.get(letra) - 1);
                    freqt.put(Character.toUpperCase(letra), freqt.get(Character.toUpperCase(letra)) - 1);
                } else if (Character.isUpperCase(letra) && freqt.containsKey(Character.toLowerCase(letra)) && freqt.get(Character.toLowerCase(letra)) > 0) {
                    whoops++;
                    freqs.put(letra, freqs.get(letra) - 1);
                    freqt.put(Character.toLowerCase(letra), freqt.get(Character.toLowerCase(letra)) - 1);
                } else {
                    break;
                }
            }
        }
        System.out.println(yay + " " + whoops);
    }
}
```

Please note that in Java, you need to import the `java.util.Scanner` and `java.util.HashMap` classes to use the `Scanner` and `HashMap` classes respectively. Also, the `getOrDefault` method is used instead of the `get` method to avoid a `NullPointerException` when the key is not present in the map.
<|EOT|>
