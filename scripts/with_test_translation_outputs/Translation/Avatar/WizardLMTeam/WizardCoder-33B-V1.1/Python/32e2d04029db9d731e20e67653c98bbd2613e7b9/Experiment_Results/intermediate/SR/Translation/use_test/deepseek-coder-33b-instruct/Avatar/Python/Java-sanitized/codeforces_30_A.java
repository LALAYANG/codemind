import java.util.Scanner;

public class codeforces_30_A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int n = scanner.nextInt();
        System.out.println(task4(A, B, n));
    }

    public static int task4(int A, int B, int n) {
        for (int X = -1000; X <= 1000; X++) {
            if (A * Math.pow(X, n) == B) {
                return X;
            }
        }
        return -1001; // return a value that is not a valid solution
    }
}