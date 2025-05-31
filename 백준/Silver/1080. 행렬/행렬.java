import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static String[][] matrixA;
    public static String[][] matrixB;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] matrix = br.readLine().split(" ");
        int N = Integer.parseInt(matrix[0]);
        int M = Integer.parseInt(matrix[1]);

        matrixA = new String[N][M];
        matrixB = new String[N][M];

        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split("");
            matrixA[i] = tmp;
        }

        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split("");
            matrixB[i] = tmp;
        }

        int result = greedy(N, M);

        System.out.println(result);

    }

    public static int greedy(int N, int M) {
        if (N < 3 || M < 3) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (!matrixA[i][j].equals(matrixB[i][j])) {
                        return -1;
                    }
                }
            }
        }

        int cnt = 0;

        for (int i = 0; i < N-2; i++) {
            for (int j = 0; j < M-2; j++) {
                if (!matrixA[i][j].equals(matrixB[i][j])) {
                    change3x3(i,j);
                    cnt ++;
                }
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!matrixA[i][j].equals(matrixB[i][j])) {
                    return -1;
                }
            }
        }
        
        return cnt;
    }

    private static void change3x3(int i, int j) {
        for (int k = 0; k < 3; k++) {
            for (int l = 0; l < 3; l++) {
                if (matrixA[i+k][j+l].equals("0")) {
                    matrixA[i+k][j+l] = "1";
                }else if (matrixA[i+k][j+l].equals("1")) {
                    matrixA[i+k][j+l] = "0";
                }
            }
        }
    }
}
