#include <stdio.h>
#include <string>
#include <iostream>

int main(){
	std::string st="122";
	st += std::string(st[2] - '0', st.back() ^ 3);
	std::cout << st << '\n';
}
