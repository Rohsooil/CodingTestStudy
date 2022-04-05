import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class Q42842 {

    public int[] solution(int brown, int yellow) {

        List<int[]> division = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        IntStream.range(1, Double.valueOf(Math.sqrt(Integer.valueOf(yellow).doubleValue())).intValue() + 1)
                .filter(i -> yellow % i == 0).forEach(i -> {
                    division.add(new int[]{i, yellow / i});
                });

        division.forEach(arr -> {
            var squareWidth = (arr[0] + 2) * (arr[1] + 2);
            var yellowWidth = arr[0] * arr[1];

            if (brown == squareWidth - yellowWidth) {
                answer.add(arr[1] + 2);
                answer.add(arr[0] + 2);
                return;
            }
        });

        return answer.stream().mapToInt(i -> i).toArray();
    }

}
