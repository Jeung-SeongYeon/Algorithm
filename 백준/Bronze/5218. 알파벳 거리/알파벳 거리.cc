#include <iostream>

int main(){
    int N;
    std::cin >> N;
    std::string first, second;
    for (; N > 0; N--){
        std::cin >> first >> second;
        std::cout << "Distances:";
        for (int i = 0; i < first.size(); i++){
            int a = second[i] - first[i];
            if (a < 0){
                a = a + 26;
            }
            std::cout << " " << a;
        }
        std::cout << "\n";
    }
}