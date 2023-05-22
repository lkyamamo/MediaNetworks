#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void replaceTextInFile(const string& inputFile, const string& outputFile, const string& targetText, const string& replacementText) {
    ifstream file(inputFile);
    ofstream newFile(outputFile);
    string line;

    while (getline(file, line)) {
        size_t pos = line.find(targetText);
        while (pos != string::npos) {
            line.replace(pos, targetText.length(), replacementText);
            pos = line.find(targetText, pos + replacementText.length());
        }
        newFile << line << "\n";
    }

    file.close();
    newFile.close();
}

int main() {
    string inputFile = "input.txt";
    string outputFile = "output.txt";
    string targetText = "old text";
    string replacementText = "new text";

    replaceTextInFile(inputFile, outputFile, targetText, replacementText);

    cout << "Text replacement complete. Output saved to " << outputFile << endl;

    return 0;
}
