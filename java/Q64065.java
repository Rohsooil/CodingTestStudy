import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Q64065 {
    public int[] solution(String s) {

        List<Integer> numbers = new ArrayList<>();
        List<List<Integer>> tuples = new ArrayList<>();
        boolean opened = false;
        String number = "";

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '{') {
                opened = true;
            } else if (s.charAt(i) == ',') {
                if (opened) {
                    numbers.add(Integer.valueOf(number));
                    number = "";
                }
            } else if (s.charAt(i) == '}') {
                opened = false;
                numbers.add(Integer.valueOf(number));
                number = "";
                tuples.add(numbers);
                numbers = new ArrayList<>();
            } else {
                number += s.charAt(i);
            }
        }
        tuples.sort(Comparator.comparing(t -> Integer.valueOf(t.size())));

        List<Integer> answer = new ArrayList<>();
        for (List<Integer> list : tuples) {
            for (Integer element : list) {
                if (!answer.contains(element)) {
                    answer.add(element);
                    break;
                }
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        System.out.println(String.join(", ",
                IntStream.of(new Q64065().solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
                        .mapToObj(String::valueOf).collect(Collectors.toList())));
    }

}
