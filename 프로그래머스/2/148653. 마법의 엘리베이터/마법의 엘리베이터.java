import java.util.*;

class Solution {
    int[] dp;

    public void init(int n, int k){
        if (k==-1) {
            return;
        }
        int start = (int) (n - Math.pow(10,k+1));
        int end = n;
        
        for (int j=0; j<10; j++) {
            int num = (int) ((j+1) * Math.pow(10,k));

            if (dp[start + num] == 0 ){
                dp[start + num] = Math.min(dp[start]+(j+1), dp[end]+(9-j));
            }

            init(start + num,k-1);
        }
    }

    public int solution(int storey) {
        int i = 1;
        int c = -1;

        while (i < storey){
            i *= 10;
            c ++;
        }

        dp = new int[i+1];
        dp[i] = 1;

        init((int) Math.pow(10,c+1),c);
        
        return dp[storey];
    }
}