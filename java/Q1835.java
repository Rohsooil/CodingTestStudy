import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Q1835 {

    private final String less = "<";
    private final String more = ">";
    private final String equal = "=";

    int answer = 0;

    class Condition {
        String left;
        String right;
        String operator;
        int distance;

        Condition(String left, String right, String operator, int distance) {
            this.left = left;
            this.right = right;
            this.operator = operator;
            this.distance = distance;
        }
    }


    public int solution(int n, String[] data) {
        List<String> friends = Arrays.asList(new String[]{"A", "C", "F", "J", "M", "N", "R", "T"});
        int[] positions = new int[friends.size()];
        boolean[] visited = new boolean[friends.size()];
        List<Condition> conditions = Arrays.stream(data).map(this::toCondition).collect(Collectors.toList());
        loop(0, friends, positions, visited, conditions);

        return answer;
    }

    private Condition toCondition(String data) {
        String[] splited = data.split("");
        return new Condition(splited[0], splited[2], splited[3], Integer.valueOf(splited[4]));
    }

    private void loop(int depth, List<String> friends, int[] positions, boolean[] visited, List<Condition> conditions) {

        if (depth == friends.size()) {
            if (passedConditions(friends, positions, conditions)) {
                answer++;
            }
            return;
        }

        for (int i = 0; i < friends.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                positions[depth] = i;
                loop(depth + 1, friends, positions, visited, conditions);
                visited[i] = false;
            }
        }
    }

    private boolean passedConditions(List<String> friends, int[] positions, List<Condition> conditions) {

        for (Condition condition : conditions) {
            int leftConditionPosition = positions[friends.indexOf(condition.left)];
            int rightConditionPosition = positions[friends.indexOf(condition.right)];

            switch (condition.operator) {
                case equal:
                    if (Math.abs(leftConditionPosition - rightConditionPosition) - 1 != condition.distance) {
                        return false;
                    }
                    break;
                case less:
                    if (Math.abs(leftConditionPosition - rightConditionPosition) - 1 >= condition.distance) {
                        return false;
                    }
                    break;
                case more:
                    if (Math.abs(leftConditionPosition - rightConditionPosition) - 1 <= condition.distance) {
                        return false;
                    }
                    break;
                default:
                    break;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int solution = new Q1835().solution(2, new String[]{"N~F=0", "R~T>2"});
        int solution2 = new Q1835().solution(2, new String[]{"M~C<2", "C~M>1"});
        System.out.println(solution);
        System.out.println(solution2);
    }

}
