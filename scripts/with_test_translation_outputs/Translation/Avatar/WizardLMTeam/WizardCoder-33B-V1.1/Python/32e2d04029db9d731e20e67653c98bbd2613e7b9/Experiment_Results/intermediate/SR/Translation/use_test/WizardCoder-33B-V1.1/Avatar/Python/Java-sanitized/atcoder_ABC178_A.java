import java.util.Scanner;

public class atcoder_ABC178_A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tcs = 1;
        int tc = 1;
        while (tc <= tcs) {
            solve(scanner, tc);
            tc += 1;
        }
        scanner.close();
    }

    public static void solve(Scanner scanner, int tc) {
        int a = scanner.nextInt();
        System.out.println(a == 0 ? 1 : 0);
    }
}