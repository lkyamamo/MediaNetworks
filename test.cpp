#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

int main(){
    std::ifstream file_in("hello.txt");
    std::ofstream file_out("output.txt");

    std::stringstream ss;
    std::string line;

    std::map<std::string, int> node_map;

    // Read words from the file one by one
    while (std::getline(file_in, line)) {
        //get the mapped value of this word 
        ss << line;
        std::string key;
        std::string value;

        ss >> key;
        ss >> value;

        std::cout << key << " " << value;

        node_map.insert(std::pair<std::string, int> (key, std::stoi(value)));
    }

    std::cout << node_map["hello"];

    return 0;
}
    