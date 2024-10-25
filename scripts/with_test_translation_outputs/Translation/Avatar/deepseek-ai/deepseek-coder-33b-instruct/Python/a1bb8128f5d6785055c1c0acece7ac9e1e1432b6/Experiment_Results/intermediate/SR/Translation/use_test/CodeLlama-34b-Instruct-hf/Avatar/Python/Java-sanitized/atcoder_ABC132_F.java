import java.util.Scanner;

public class atcoder_ABC132_F {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int mod = 1000000007;

        int[] coef = new int[n];
        for (int i = 1; i <= n; i++) {
            coef[i - 1] = (n / i) - (n / (i + 1));
        }
        coef[n - 1] = 1;

        int[][] dp = new int[k + 1][n];
        dp[0][0] = 1;
        for (int i = 1; i <= k; i++) {
            int tmp = 0;
            for (int j = n - 1; j >= 0; j--) {
                tmp += dp[i - 1][(n - 1) - j];
                tmp %= mod;
                dp[i][j] = coef[j] * tmp;
                dp[i][j] %= mod;
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            result += dp[k][i];
            result %= mod;
        }

        System.out.println(result);
    }
}