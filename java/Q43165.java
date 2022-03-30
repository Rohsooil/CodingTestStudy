public class Q43165 {

    public int answer;

    public int solution(int[] numbers, int target) {

        loop(numbers, target, 0, 0);
        return answer;
    }

    public void loop(int[] numbers, int target, int sum, int depth) {

        if (numbers.length == depth) {
            if (sum == target) {
                answer++;
            }
            return;
        }
        loop(numbers, target, sum + numbers[depth], depth + 1);
        loop(numbers, target, sum - numbers[depth], depth + 1);
    }

    public static void main(String[] args) {
        int solution = new Q43165().solution(new int[]{1, 1, 1, 1, 1}, 3);
        System.out.println(solution);
    }

}
