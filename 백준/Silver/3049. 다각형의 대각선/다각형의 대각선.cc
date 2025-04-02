#include <iostream>

int facto(int x){
    int result = x*(x-1)*(x-2)*(x-3)/24;
    return result;
}

int main(){
    int N;
    std::cin >> N;
    if (N==3){
        std::cout << 0;
    }else{
    std::cout << facto(N);
    }
}