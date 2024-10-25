import java.util.Collections;
import java.util.List;
import java.util.Map;

public class atcoder_ABC110_C {
    public static void main(String[] args) {
        String s = "chokudai";
        String t = "redcoder";
        System.out.println(run(s, t));
    }

    public static String run(String s, String t) {
        Map<Character, Integer> sMap = countCharacters(s);
        Map<Character, Integer> tMap = countCharacters(t);
        List<Integer> sList = new ArrayList<>(sMap.values());
        List<Integer> tList = new ArrayList<>(tMap.values());
        Collections.sort(sList);
        Collections.sort(tList);
        if (sList.equals(tList)) {
            return "Yes";
        } else {
            return "No";
        }
    }

    public static Map<Character, Integer> countCharacters(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        return map;
    }
}