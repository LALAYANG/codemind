import java.util.Scanner;

public class codeforces_459_A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String given = scanner.nextLine();
        String[] l1 = given.split(" ");
        int x1 = Integer.parseInt(l1[0]);
        int y1 = Integer.parseInt(l1[1]);
        int x2 = Integer.parseInt(l1[2]);
        int y2 = Integer.parseInt(l1[3]);
        int denominator = x2 - x1;
        int numerator = y2 - y1;
        if (denominator != 0) {
            double quotient = (double) numerator / denominator;
            if (quotient == 1) {
                System.out.println(x1 + " " + y1 + " " + x2 + " " + y2);
            } else if (quotient == -1) {
                System.out.println(x2 + " " + y2 + " " + x1 + " " + y1);
            } else {
                System.out.println("-1");
            }
        } else if (numerator == 0) {
            int d = (int) Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
            int x3 = x1;
            int x4 = x2;
            int y3 = y2 + d;
            int y4 = y1 + d;
            System.out.println(x3 + " " + y3 + " " + x4 + " " + y4);
        } else {
            int d = (int) Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
            int x3 = x1 + d;
            int x4 = x2 + d;
            int y3 = y1;
            int y4 = y2;
            System.out.println(x3 + " " + y3 + " " + x4 + " " + y4);
        }
    }
}