#include <stdio.h>
#include <string.h>
#include "findSine.h"

// main function of the project to execute given functionallitys
int main(int argv, char* argc[]) {

	char name[] = "Ha";
	printf("%lu\n", strlen(name));
	FunctionValues object = FunctionValues(42, "testfile.txt");
	object.printValues();

	return 0;
}
