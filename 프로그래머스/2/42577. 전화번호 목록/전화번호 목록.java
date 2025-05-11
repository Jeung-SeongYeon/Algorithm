import java.util.*;

public class Solution {

    public static boolean checkPrefix(String[] phoneBook) {
        Map<Integer, List<String>> preDict = new HashMap<>();

        for (String num : phoneBook) {
            for (Integer key : preDict.keySet()) {
                for (String phone : preDict.get(key)) {
                    if (num.length() > key && num.substring(0, key).equals(phone)) {
                    return false;
                    }
                }
            }
        preDict.put(num.length(), new ArrayList<>(Arrays.asList(num)));
        }

    return true;
    }

    public static boolean solution(String[] phoneBook) {
        Arrays.sort(phoneBook);
        return checkPrefix(phoneBook);
    }
}