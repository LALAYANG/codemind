import java.util.*;

public class atcoder_ABC155_E {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        int pp = 0;
        int na = 0;
        for (int i = 0; i < s.length(); i++) {
            int cc = na + Integer.parseInt(String.valueOf(s.charAt(i)));
            na = 0;
            if (cc <= 4) {
                pp += cc;
            } else {
                na = 1;
                if (i == s.length() - 1) {
                    pp += 1;
                }
                pp += 10 - cc;
            }
        }
        System.out.println(pp);
    }
}