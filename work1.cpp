#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

string parse_stream(istream &stream) 
{
	string line;
	while (getline(cin, line))
	{
		if (!line.length()) 
		{
		ostringstream ss;
		ss << stream.rdbuf();
		return ss.str();
		}
	}
	return string();
}

int main() {
	ifstream file("http.dat");
	string result = parse_stream(file);
	cout << result;
	return 0;
}