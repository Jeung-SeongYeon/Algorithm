#include <iostream>

int main(){
    while (1){
        std::string input;
        getline(std::cin, input);
        if (input == "END"){
            break;
        }
        for (int i = input.size()-1; i >= 0; i--){
            std::cout << input[i];
        }
        std::cout << "\n";
    }
}