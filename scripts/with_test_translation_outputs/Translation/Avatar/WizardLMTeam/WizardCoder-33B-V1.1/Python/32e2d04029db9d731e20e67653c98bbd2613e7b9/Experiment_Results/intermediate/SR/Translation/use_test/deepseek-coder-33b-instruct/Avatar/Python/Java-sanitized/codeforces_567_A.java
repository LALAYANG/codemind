import java.util.Scanner;

public class codeforces_567_A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                System.out.println((arr[i + 1] - arr[i]) + " " + (arr[n - 1] - arr[i]));
                continue;
            }
            if (i == n - 1) {
                System.out.println((arr[n - 1] - arr[n - 2]) + " " + (arr[n - 1] - arr[0]));
                continue;
            }
            if (arr[i] - arr[i - 1] > arr[i + 1] - arr[i]) {
                System.out.print(arr[i + 1] - arr[i] + " ");
            } else {
                System.out.print(arr[i] - arr[i - 1] + " ");
            }
            if (arr[n - 1] - arr[i] > arr[i] - arr[0]) {
                System.out.println(arr[n - 1] - arr[i]);
            } else {
                System.out.println(arr[i] - arr[0]);
            }
        }
    }
}