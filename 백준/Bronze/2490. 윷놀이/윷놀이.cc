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

std::string yut(int x){
    if (x == 0){
        return "E";
    }else if (x == 1){
        return "A";
    }else if (x == 2){
        return "B";
    }else if (x == 3){
        return "C";
    }else if (x == 4){
        return "D";
    }
}

int main(){
    std::string str;
    for (int i = 3; i > 0; i--){
        int cnt = 0;
        std::string result;
        getline(std::cin, str);
        std::vector<std::string> li = split(str, ' ');
        for (int j = 0; j < li.size(); j++){
            if (stoi(li[j]) == 0){
                cnt = cnt + 1;
            }
        }
        result = yut(cnt);
        std::cout << result << "\n";
    }
}