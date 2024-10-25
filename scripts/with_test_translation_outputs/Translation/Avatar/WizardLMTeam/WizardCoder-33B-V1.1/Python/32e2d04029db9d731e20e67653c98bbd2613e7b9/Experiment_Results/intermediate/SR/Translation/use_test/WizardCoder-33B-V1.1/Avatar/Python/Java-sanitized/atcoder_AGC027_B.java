import java.util.*;

public class atcoder_AGC027_B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int X = scanner.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        long[] S = new long[N];
        S[0] = A[0];
        for (int i = 1; i < N; i++) {
            S[i] = S[i - 1] + A[i];
        }
        long ans = Long.MAX_VALUE;
        for (int k = 0; k < N; k++) {
            long E = (k + 1) * X + 2 * sum(S, N, k + 1);
            ans = Math.min(ans, E);
        }
        System.out.println(ans + N * X + 5 * S[N - 1]);
    }

    private static long sum(long[] S, int N, int k) {
        long sum = 0;
        for (int j = N - 2 * k - 1; j >= 0; j -= k) {
            sum += S[j];
        }
        return sum;
    }
}