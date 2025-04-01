import java.util.*;

public class Main {
    public static void main(String[] args){
        int n;

        Scanner N = new Scanner(System.in);
        n = N.nextInt();
        N.close();
        for(int i=n;i >= 1;i-=1) {
            String star = "*";
            star = star.repeat(i);
            System.out.println(star);
        }
    }
}