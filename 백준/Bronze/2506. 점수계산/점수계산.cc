#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::vector<std::string> split(std::string input, char delim){
    std::vector<std::string> answer;
    std::stringstream ss(input);
    std::string temp;
    while (getline(ss, temp, delim)){
        answer.push_back(temp);
    }
    return answer;
}

int main(){
    int N;
    std::cin >> N;
    std::cin.ignore();

    int point = 0;
    int result = 0;
    std::string str;
    getline(std::cin, str);
    std::vector<std::string> array = split(str, ' ');
    for (int i = 0; i < N; i++){
        if (stoi(array[i]) == 1){
            point = point + 1;
            result = result + point;
        }else{
            point = 0;
        }
    }
    std::cout << result;
}