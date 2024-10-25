public class codeforces_30_A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int A = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);
        int n = Integer.parseInt(input[2]);

        for (int X = -1000; X <= 1000; X++) {
            if (A * (X ^ n) == B) {
                System.out.println(X);
                return;
            }
        }
        System.out.println("No solution");
    }
}