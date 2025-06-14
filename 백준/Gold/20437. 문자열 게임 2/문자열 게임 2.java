import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split("");
            int K = Integer.parseInt(br.readLine());
            int[] result = queue(s,K);
            if (result[2] == -1) {
                System.out.println(-1);
            } else {
                System.out.println(result[0] + " " + result[1]);
            }
        }
    }

    public static int[] queue(String[] s, int K) {
        Map<String, Queue<Integer>> targets = new HashMap<>();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int cnt = -1;
        
        for (int i = 0; i < s.length; i++) {
            Queue<Integer> target = targets.get(s[i]);
            if (target == null) {
                target = new LinkedList<>();
                target.offer(i);
                targets.putIfAbsent(s[i], target);
            } else {
                target.offer(i);
            }
            if (target.size() == K) {
                min = Math.min(min, i - target.peek() + 1);
                max = Math.max(max, i - target.peek() + 1);
                target.poll();
                cnt++;
            }
        }
        return new int[]{min, max, cnt};
    }
}