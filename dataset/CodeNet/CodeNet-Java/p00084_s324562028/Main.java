import java.util.*;class Main{public static void main(String[]z){String s="";for(String x:new Scanner(System.in).nextLine().split("[ .,]"))if(x.matches(".{3,6}"))s+=x+" ";System.out.println(s.replaceAll(" $",""));}}