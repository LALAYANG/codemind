import java.util.*;

public class atcoder_ABC110_C {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        String t = scanner.next();
        System.out.println(run(s, t));
    }

    public static String run(String s, String t) {
        Map<Character, Integer> sCount = new HashMap<>();
        Map<Character, Integer> tCount = new HashMap<>();

        for (char c : s.toCharArray()) {
            sCount.put(c, sCount.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            tCount.put(c, tCount.getOrDefault(c, 0) + 1);
        }

        List<Integer> ss = new ArrayList<>(sCount.values());
        List<Integer> tt = new ArrayList<>(tCount.values());

        Collections.sort(ss);
        Collections.sort(tt);

        if (ss.equals(tt)) {
            return "Yes";
        } else {
            return "No";
        }
    }
}