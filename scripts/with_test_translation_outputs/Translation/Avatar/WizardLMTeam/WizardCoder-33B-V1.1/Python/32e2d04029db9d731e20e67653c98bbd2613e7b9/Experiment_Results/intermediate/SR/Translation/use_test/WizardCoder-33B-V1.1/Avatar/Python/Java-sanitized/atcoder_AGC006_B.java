import java.util.*;

public class atcoder_AGC006_B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int X = scanner.nextInt();

        if (X == 1 || X == N * 2 - 1) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
            if (X == N * 2 - 2) {
                ArrayList<Integer> xs = new ArrayList<>();
                for (int i = N - 1; i <= X + 2; i++) {
                    xs.add(i);
                }
                for (int i = 1; i < N - 1; i++) {
                    xs.add(i);
                }
                for (int i : xs) {
                    System.out.println(i);
                }
            } else {
                ArrayList<Integer> ys = new ArrayList<>();
                for (int i = 1; i < X - 1; i++) {
                    ys.add(i);
                }
                for (int i = X + 3; i <= N * 2; i++) {
                    ys.add(i);
                }
                ArrayList<Integer> xs = new ArrayList<>();
                for (int i = 0; i < N - 3; i++) {
                    xs.add(ys.get(i));
                }
                xs.add(X + 2);
                xs.add(X - 1);
                xs.add(X);
                xs.add(X + 1);
                for (int i = N - 3; i < ys.size(); i++) {
                    xs.add(ys.get(i));
                }
                for (int i : xs) {
                    System.out.println(i);
                }
            }
        }
    }
}