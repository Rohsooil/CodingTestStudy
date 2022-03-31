import java.util.HashSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Q12981 {


    public int[] solution(int n, String[] words) {

        HashSet<String> wordSets = new HashSet<>();
        String previous = "";
        for (int i = 0; i < words.length; i++) {
            int personIndex = i % n;
            String word = words[i];

            if ((previous.length() != 0 && !word.startsWith("" + previous.charAt(previous.length() - 1)))
                    || wordSets.contains(word)) {
                return new int[]{personIndex + 1, i / n + 1};
            }

            wordSets.add(word);
            previous = word;
        }

        return new int[]{0, 0};
    }

    public static void main(String[] args) {

        int[] solution = new Q12981().solution(3, new String[]{"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"});
        System.out.println(String.join(", ", IntStream.of(solution).mapToObj(String::valueOf).collect(Collectors.toList())));
        int[] solution2 = new Q12981().solution(2, new String[]{"hello", "one", "even", "never", "now", "world", "draw"});
        System.out.println(String.join(", ", IntStream.of(solution2).mapToObj(String::valueOf).collect(Collectors.toList())));
    }

}
