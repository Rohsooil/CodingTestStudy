public class Q12911 {

    public int solution(int n) {

        String binary = Integer.toBinaryString(n);
        int binaryOneCount = count(binary);
        int nextNumber = n + 1;
        int answer = 0;

        while (true) {
            String nextBinary = Integer.toBinaryString(nextNumber);
            int nextBinaryOneCount = count(nextBinary);
            if (binaryOneCount == nextBinaryOneCount) {
                answer = nextNumber;
                break;
            }
            nextNumber++;
        }

        return answer;
    }

    private int count(String binary) {
        int count = 0;
        char[] charArr = binary.toCharArray();
        for (char ch : charArr) {
            if (ch == '1') {
                count++;
            }
        }
        return count;
    }

}
