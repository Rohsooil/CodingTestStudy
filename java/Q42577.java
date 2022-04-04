import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

public class Q42577 {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> map = Arrays.stream(phone_book).collect(Collectors.toMap(String::valueOf, str -> Integer.valueOf(1)));

        for (String phone : phone_book) {
            String temp = "";
            for (String number : phone.split("")) {
                temp += number;
                if (map.containsKey(temp) && !temp.equals(number)) {
                    return false;
                }
            }
        }
        return true;
    }
}
