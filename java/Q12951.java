import java.util.ArrayList;
import java.util.List;

public class Q12951 {
    public String solution(String s) {

        List<String> stringList = new ArrayList<>();
        for (String str : s.split(" ")) {
            if (str.equals("")) {
                stringList.add("");
                continue;
            }

            if (str.length() == 1) {
                str = str.toUpperCase();
            } else {
                str = str.toLowerCase();
                str = String.valueOf(str.charAt(0)).toUpperCase() + str.substring(1);
            }
            stringList.add(str);
        }

        return String.join(" ", stringList) + (String.valueOf(s.charAt(s.length() - 1)).equals(" ") ? " " : "");
    }

    public static void main(String[] args) {
        System.out.println(new Q12951().solution("3people Unfollowed Me "));
    }

}
