import java.util.*;

public class Main {
    public static void main(String[] args){
        int n;

        Scanner N = new Scanner(System.in);
        n = N.nextInt();
        N.close();
        for(int i=n-1;i >= 0;i-=1) {
            String empty = " ";
            String star = "*";
            empty = empty.repeat(i);
            star = star.repeat(n-i);
            System.out.println(empty + star);
        }
    }
}