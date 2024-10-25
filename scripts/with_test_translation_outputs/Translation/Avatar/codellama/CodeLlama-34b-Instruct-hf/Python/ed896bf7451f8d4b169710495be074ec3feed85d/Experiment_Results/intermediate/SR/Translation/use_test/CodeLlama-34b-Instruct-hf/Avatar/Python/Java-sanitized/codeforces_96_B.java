import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class codeforces_96_B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int limit = 1000000000;
        ArrayList<Integer> l = new ArrayList<>();
        gen(0, 0, 0, limit, l);
        Collections.sort(l);
        int n = sc.nextInt();
        int ans = 0;
        for (int val : l) {
            if (val >= n) {
                ans = val;
                break;
            }
        }
        System.out.println(ans);
    }

    public static void gen(int number, int four, int seven, int limit, ArrayList<Integer> l) {
        if (number > limit) {
            return;
        }
        if (number > 0 && four == seven) {
            l.add(number);
        }
        gen(number * 10 + 4, four + 1, seven, limit, l);
        gen(number * 10 + 7, four, seven + 1, limit, l);
    }
}