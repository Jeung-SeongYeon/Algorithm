#include <iostream>

int main(){
    int N;
    std::cin >> N;
    int a = 0;
    int b;
    for (int i = N; i > 0; i--){
        std::cin >> b;
        a = a + b;
    }
    std::cout << a - N + 1;
}