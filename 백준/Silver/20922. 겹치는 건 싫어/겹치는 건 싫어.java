import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] config = br.readLine().split(" ");

        int N = Integer.parseInt(config[0]);
        int K = Integer.parseInt(config[1]);

        String[] targetArray = br.readLine().split(" ");

        int result = twoPointer(targetArray, N, K);
        System.out.println(result);
    }

    public static int twoPointer(String[] arr, int N, int K) {
        int start = 0;
        int end = 0;

        int[] numArray = new int[100001];
        
        int max = 0;
        
        while (start <= end && end < N) {
            int targetIndex = Integer.parseInt(arr[end]);
            numArray[targetIndex]++;
            while (numArray[targetIndex] > K) {
                numArray[Integer.parseInt(arr[start])]--;
                start++;
            }
            max = Math.max(max, end-start+1);
            end++;
        }


        return max;
    }
}