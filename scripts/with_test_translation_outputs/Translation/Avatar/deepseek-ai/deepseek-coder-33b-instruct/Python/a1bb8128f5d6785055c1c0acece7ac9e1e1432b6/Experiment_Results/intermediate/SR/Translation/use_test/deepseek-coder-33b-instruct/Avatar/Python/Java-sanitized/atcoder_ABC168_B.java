import java.util.Scanner;

public class atcoder_ABC168_B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int K = scanner.nextInt();
        scanner.nextLine(); // consume the newline character
        String S = scanner.nextLine();
        System.out.println(solve(K, S));
    }

    public static String solve(int K, String S) {
        if (S.length() <= K) {
            return S;
        } else {
            return S.substring(0, K) + "...";
        }
    }
}