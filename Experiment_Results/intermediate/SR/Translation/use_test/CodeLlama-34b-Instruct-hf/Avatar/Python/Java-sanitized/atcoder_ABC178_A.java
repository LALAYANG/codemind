import java.util.Scanner;

public class atcoder_ABC178_A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();
        while (tc > 0) {
            int a = scanner.nextInt();
            if (a == 0) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
            tc--;
        }
    }
}