import java.util.stream.IntStream;

public class Q12913 {

    private int indexOf(int number) {

        return number >= 0 ? number : 4 + number;
    }

    int solution(int[][] land) {

        for (int i = 1; i < land.length; i++) {
            for (int j = 0; j < 4; j++) {
                land[i][j] = IntStream.of(land[i - 1][indexOf(j - 1)], land[i - 1][indexOf(j - 2)],
                        land[i - 1][indexOf(j - 3)]).max().getAsInt() + land[i][j];
            }
        }

        return IntStream.of(land[land.length - 1]).max().getAsInt();
    }

}
