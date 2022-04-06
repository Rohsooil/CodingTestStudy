import java.util.*;
import java.util.stream.Collectors;

public class Q72411 {
    public String[] solution(String[] orders, int[] course) {

        List<String> answer = new ArrayList<>();
        for (int number : course) {
            Map<String, Integer> resultMap = new HashMap<>();

            for (String order : orders) {
                String[] arr = order.split("");
                Arrays.sort(arr);
                List<List<String>> resultList = new ArrayList<>();
                combination(resultList, arr, new boolean[arr.length], 0, arr.length, number);
                for (List<String> result : resultList) {
                    String combined = String.join("", result);
                    if (resultMap.containsKey(combined)) {
                        resultMap.put(combined, resultMap.get(combined) + 1);
                    } else {
                        resultMap.put(combined, 1);
                    }
                }
            }

            if (!resultMap.isEmpty()) {
                OptionalInt maxFrequency = resultMap.values().stream().mapToInt(i -> i).max();
                if (maxFrequency.isPresent() && maxFrequency.getAsInt() != 1) {
                    resultMap.forEach((key, value) -> {
                        if (value.equals(maxFrequency.getAsInt())) {
                            answer.add(key);
                        }
                    });
                }
            }
        }
        Collections.sort(answer);
        return answer.toArray(new String[answer.size()]);
    }

    private void combination(List<List<String>> result, String[] arr, boolean[] visited, int depth, int n, int r) {
        if (r == 0) {
            List<String> combinated = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (visited[i]) {
                    combinated.add(arr[i]);
                }
            }
            result.add(combinated);
            return;
        }

        if (depth == n) {
            return;
        }

        visited[depth] = true;
        combination(result, arr, visited, depth + 1, n, r - 1);

        visited[depth] = false;
        combination(result, arr, visited, depth + 1, n, r);
    }

    public static void main(String[] args) {
        String[] solution = new Q72411()
                .solution(new String[]{"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"}, new int[]{2, 3, 4});
        System.out.println(String.join(", ", Arrays.stream(solution).collect(Collectors.toList())));
    }

}
