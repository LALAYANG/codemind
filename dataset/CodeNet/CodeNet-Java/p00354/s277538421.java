import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("thu:fri:sat:sun:mon:tue:wed".split(":")[sc.nextInt()%7]);
    }
}
