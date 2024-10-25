import java.util.Scanner;

public class atcoder_ABC043_B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String myStr = "";
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '0' || c == '1') {
                myStr += c;
            } else if (c == 'B' && myStr.length() != 0) {
                myStr = myStr.substring(0, myStr.length() - 1);
            }
        }
        System.out.println(myStr);
    }
}