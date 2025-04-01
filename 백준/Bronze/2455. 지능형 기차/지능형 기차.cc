#include <iostream>

int main(){
    int max = 0;
    int recent = 0;
    int out, in;
    for (int i = 4; i > 0; i--){
        std::cin >> out >> in;
        recent = recent - out + in;
        if (max < recent){
            max = recent;
        }
    }
    std::cout << max;
}