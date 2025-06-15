#include <iostream>

int main(){
    char str[101];
    std::cin.getline(str, sizeof(str));
    for (int i = 0; i < sizeof(str); i++){
        if (65 <= str[i] && str[i] <= 90){
            str[i] = (str[i]-65 + 13)%26 + 65;
        }else if (97 <= str[i] && str[i] <= 122){
            str[i] = (str[i]-97 + 13)%26 + 97;
        }
    }
    std::cout << str;
}