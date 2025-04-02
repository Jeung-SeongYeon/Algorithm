#include <iostream>

int main(){
    int N;
    int a = 0;
    int b = 100;
    for (int i = 7; i > 0; i--){
        std::cin >> N;
        if (N % 2 == 1){
            a = a + N;
            if (N < b){
                b = N;
            }
        }
    }
    if (a == 0){
        std::cout << -1;
    } else{
        std::cout << a << "\n" << b;
    }
}