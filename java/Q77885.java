import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class Q77885 {

    public long[] solution(long[] numbers) {

        return LongStream.of(numbers).map(this::findNumber).toArray();
    }

    private long findNumber(long number) {
        if (number % 2 == 0) {
            return number + 1;
        }

        String binary = Long.toBinaryString(number);
        if (binary.indexOf('0') == -1) {
            binary = "10" + binary.substring(1);
            return Long.parseLong(binary, 2);
        }

        int lastIndexOfZero = binary.lastIndexOf('0');
        if (lastIndexOfZero + 2 >= binary.length()) {
            binary = binary.substring(0, lastIndexOfZero) + "10";
        } else {
            binary = binary.substring(0, lastIndexOfZero) + "10" + binary.substring(lastIndexOfZero + 2);
        }
        return Long.parseLong(binary, 2);
    }

    public static void main(String[] args) {

        System.out.println(String.join(",", LongStream.of(new Q77885().solution(new long[]{2, 7}))
                .mapToObj(String::valueOf).collect(Collectors.toList())));
    }
}