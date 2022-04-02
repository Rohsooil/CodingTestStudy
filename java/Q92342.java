import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class Q92342 {

    private final int NUMBER_OF_TARGET = 11;
    private List<int[]> rionWinRecords = new ArrayList<>();
    private int maxDiff;

    class Result {
        int diff;
        boolean rionWin;

        Result(int diff, boolean rionWin) {
            this.diff = diff;
            this.rionWin = rionWin;
        }
    }

    public int[] solution(int n, int[] info) {
        loop(0, new int[info.length], info, n);
        return findAnswer();
    }

    private void loop(int depth, int[] rion, int[] peach, int numberOfArrow) {

        if (depth == NUMBER_OF_TARGET || numberOfArrow == 0) {
            rion[10] += numberOfArrow;
            Result result = result(rion, peach);
            if (result.rionWin) {
                if (result.diff > maxDiff) {
                    maxDiff = result.diff;
                    rionWinRecords = new ArrayList<>(Arrays.asList(Arrays.copyOf(rion, rion.length)));
                } else if (result.diff == maxDiff) {
                    rionWinRecords.add(Arrays.copyOf(rion, rion.length));
                }
            }
            rion[10] -= numberOfArrow;
            return;
        }

        if (peach[depth] < numberOfArrow) {
            rion[depth] += peach[depth] + 1;
            loop(depth + 1, rion, peach, numberOfArrow - (peach[depth] + 1));
            rion[depth] -= peach[depth] + 1;
        }
        loop(depth + 1, rion, peach, numberOfArrow);
    }

    private Result result(int[] rion, int[] peach) {

        int rionScore = 0;
        int peachScore = 0;

        for (int i = 0; i < NUMBER_OF_TARGET; i++) {
            int rionHit = rion[i];
            int peachHit = peach[i];

            if (rionHit == 0 && peachHit == 0) {
                continue;
            }

            if (rionHit > peachHit) {
                rionScore += (NUMBER_OF_TARGET - 1 - i);
            } else {
                peachScore += (NUMBER_OF_TARGET - 1 - i);
            }
        }
        return new Result(Math.abs(rionScore - peachScore), rionScore > peachScore);
    }

    private int[] findAnswer() {

        if (rionWinRecords.isEmpty()) {
            return new int[]{-1};
        }

        if (rionWinRecords.size() == 1) {
            return rionWinRecords.get(0);
        }

        int[] answer = rionWinRecords.get(0);

        for (int i = 1; i < rionWinRecords.size(); i++) {
            int[] answerCandidate = rionWinRecords.get(i);
            for (int j = 10; j >= 0; j--) {
                if (answerCandidate[j] > answer[j]) {
                    answer = answerCandidate;
                    break;
                } else if (answerCandidate[j] < answer[j]) {
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        IntStream.of(new Q92342().solution(5, new int[]{2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0})).forEach(System.out::print);
        //IntStream.of(new Q92342().solution(1, new int[]{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0})).forEach(System.out::print);
    }

}
