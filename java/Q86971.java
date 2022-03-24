import java.util.LinkedList;
import java.util.Queue;

public class Q86971 {
    public int solution(int n, int[][] wires) {

        int answer = n;
        int[][] arr = new int[n + 1][n + 1];
        for (int i = 0; i < wires.length; i++) {
            arr[wires[i][0]][wires[i][1]] = 1;
            arr[wires[i][1]][wires[i][0]] = 1;
        }
        int a, b;
        for (int i = 0; i < wires.length; i++) {
            a = wires[i][0];
            b = wires[i][1];

            arr[a][b] = 0;
            arr[b][a] = 0;

            answer = Math.min(answer, bfs(n, a, arr));

            arr[a][b] = 1;
            arr[b][a] = 1;
        }

        return answer;
    }

    public int bfs(int n, int start, int[][] arr) {
        int[] visit = new int[n + 1];
        int cnt = 1;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            int point = queue.poll();
            visit[point] = 1;

            for (int i = 1; i <= n; i++) {
                if (visit[i] == 1) {
                    continue;
                }
                if (arr[point][i] == 1) {
                    queue.offer(i);
                    cnt++;
                }
            }
        }
        return (int) Math.abs(n - 2 * cnt);
    }

    public static void main(String[] args) {
        int solution = new Q86971().solution(9, new int[][]{{1, 3}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {4, 7}, {7, 8}, {7, 9}});
        System.out.println(solution);
    }

}
