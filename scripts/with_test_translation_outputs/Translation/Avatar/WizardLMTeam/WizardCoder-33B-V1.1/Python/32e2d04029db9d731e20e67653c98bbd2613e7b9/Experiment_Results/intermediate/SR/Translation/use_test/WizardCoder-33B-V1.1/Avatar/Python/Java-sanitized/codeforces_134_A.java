import java.util.*;

public class codeforces_134_A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] w = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            w[i] = scanner.nextInt();
            sum += w[i];
        }
        List<Integer> d = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if ((sum - w[i]) / (n - 1) == w[i]) {
                d.add(i + 1);
            }
        }
        System.out.println(d.size());
        for (int i = 0; i < d.size(); i++) {
            System.out.print(d.get(i) + " ");
        }
    }
}