import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] target = new int[N];

        for (int i = 0; i < N; i++) {
            int tmp = Integer.parseInt(br.readLine());
            target[i] = tmp;
        }

        int result = binarySearch(target);
        System.out.println(N - result);
    }

    public static int binarySearch(int[] target) {
        List<Integer> list = new ArrayList<>();
        list.add(target[0]);
        for (int i = 1; i < target.length; i++) {
            if (target[i] > list.get(list.size() - 1)) {
                list.add(target[i]);
            } else {
                int start = 0;
                int end = list.size() - 1;
                while (start < end) {
                    int mid = (start + end) / 2;
                    if (list.get(mid) > target[i]) {
                        end = mid;
                    } else {
                        start = mid + 1;
                    }
                }
                list.set(end, target[i]);
            }
        }
        return list.size();
    }
}