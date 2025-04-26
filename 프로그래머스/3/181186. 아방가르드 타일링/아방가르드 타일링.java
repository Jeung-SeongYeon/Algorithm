import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        long divideNum = 1000000007;

        List<Integer> dp = new ArrayList<>();
        dp.add(1);
        dp.add(1);
        dp.add(3);
        dp.add(10);
        dp.add(23);
        dp.add(62);


        for (int i=6; i<n+1; i++) {
            long basicNum = (dp.get(i-1) + 2L *dp.get(i-2) + 6L *dp.get(i-3) + dp.get(i-4) - dp.get(i-6) + divideNum)%divideNum;

            dp.add((int) basicNum);
        }

        answer = dp.get(n);

        return answer;
    }
}