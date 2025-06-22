import java.util.*;

public class Solution {
    public int solution(int[][] scores) {
        int answer = 1;
        int targetA = scores[0][0];
        int targetB = scores[0][1];
        int targetScore = targetA + targetB;

        Arrays.sort(scores, (o1, o2) -> {
            if (o1[0] == o2[0]) return Integer.compare(o1[1], o2[1]);
            return Integer.compare(o2[0], o1[0]);
        });

        int maxB = 0;

        for (int[] score : scores) {
            int a = score[0];
            int b = score[1];

            if (a > targetA && b > targetB) {
                return -1;
            }

            if (b >= maxB) {
                maxB = b;
                if (a + b > targetScore) {
                    answer++;
                }
            }
        }

        return answer;
    }
}