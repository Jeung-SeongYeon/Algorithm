import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            String[] strArray = str.split(" ");
            for (int j = 0; j < strArray.length; j++) {
                pq.add(Integer.parseInt(strArray[j]));
            }
        }
        for (int i = 0; i < N-1; i++) {
            pq.poll();
        }
        System.out.println(pq.peek());
    }

}