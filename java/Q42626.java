import java.util.PriorityQueue;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Q42626 {

    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>(
                IntStream.of(scoville).mapToObj(Integer::valueOf).collect(Collectors.toList()));

        while (queue.peek() < K) {
            if (queue.size() == 1) {
                return -1;
            }
            int small = queue.poll();
            int nexSmall = queue.poll();
            int scovilleValue = small + nexSmall * 2;
            queue.offer(scovilleValue);
            answer++;
        }

        return answer;
    }

    public static void main(String[] args) {
        int solution1 = new Q42626().solution(new int[]{1, 2, 3, 9, 10, 12}, 7);
        System.out.println(solution1);
    }

}
