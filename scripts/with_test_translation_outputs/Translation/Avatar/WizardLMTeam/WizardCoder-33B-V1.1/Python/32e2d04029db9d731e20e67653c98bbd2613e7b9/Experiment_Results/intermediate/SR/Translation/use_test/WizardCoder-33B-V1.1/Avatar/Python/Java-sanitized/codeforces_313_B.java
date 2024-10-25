import java.util.*;

public class codeforces_313_B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String soz = scanner.nextLine();
        int[] a = new int[soz.length() + 1];
        for (int i = 1; i < soz.length(); i++) {
            a[i] = a[i - 1];
            if (soz.charAt(i - 1) == soz.charAt(i)) {
                a[i]++;
            }
        }
        int n = scanner.nextInt();
        scanner.nextLine();
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] ml = scanner.nextLine().split(" ");
            int m = Integer.parseInt(ml[0]);
            int l = Integer.parseInt(ml[1]);
            arr.add(a[l - 1] - a[m - 1]);
        }
        for (int i : arr) {
            System.out.println(i);
        }
    }
}