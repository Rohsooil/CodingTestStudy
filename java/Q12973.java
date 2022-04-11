import java.util.Stack;

public class Q12973 {

    public int solution(String s) {

        Stack<String> stack = new Stack<>();

        for (String element : s.split("")) {
            if (!stack.isEmpty() && stack.peek().equals(element)) {
                stack.pop();
            } else {
                stack.push(element);
            }
        }

        return stack.isEmpty() ? 1 : 0;
    }

}
