import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int[] dp1 = new int[10001];
    public static int[] dp2 = new int[10001];
    public static int[] dp3 = new int[10001];

    public static void init(){
        dp1[1] = 1;
        dp1[2] = 1;
        dp1[3] = 1;
        dp2[2] = 1;
        dp2[3] = 1;
        dp3[3] = 1;
    }

    public static void main(String[] args) throws IOException {
        init();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            int target = Integer.parseInt(br.readLine());
            dp(target);
            System.out.println(dp1[target] + dp2[target] + dp3[target]);
        }
    }

    private static void dp(int target) {
        for (int i = 4; i <= target; i++) {
            dp1[i] = dp1[i - 1];
            dp2[i] = dp1[i - 2] + dp2[i - 2];
            dp3[i] = dp1[i - 3] + dp2[i - 3] + dp3[i - 3];
        }
    }
}