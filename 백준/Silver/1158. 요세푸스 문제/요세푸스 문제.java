import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        int K = sc.nextInt();

        List<Integer> list = new LinkedList<Integer>();
        for (int i = 1; i < N+1; i++) {
            list.add(i);
        }

        List<Integer> result = getPermutation(list, K, N);
        StringBuffer sb = new StringBuffer();
        sb.append("<");
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));

            if (i != result.size() - 1) {
                sb.append(", ");
            }
        }
        sb.append(">");
        System.out.println(sb);
    }

    public static List<Integer> getPermutation(List<Integer> list, int K, Integer N){
        List<Integer> permutation = new ArrayList<>();
        int startIndex = 0;

        for (int i = 0; i < N; i++) {
            startIndex = (startIndex + K - 1) % list.size();
            permutation.add(list.remove(startIndex));
        }

        return permutation;
    }
}