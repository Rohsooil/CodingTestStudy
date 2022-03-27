public class Q84512 {

    public int solution(String word) {
        int answer = word.length();
        String str = "AEIOU";
        int[] x = {781, 156, 31, 6, 1};
        for (int i = 0; i < word.length(); i++) {
            int idx = str.indexOf(word.charAt(i));
            answer += x[i] * idx;
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(new Q84512().solution("I"));
        System.out.println(new Q84512().solution("A"));
        System.out.println(new Q84512().solution("AAAAE"));
    }

}
