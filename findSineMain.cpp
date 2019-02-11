#include <stdio.h>
#include <string.h>
#include "findSine.h"

// main function of the project to execute given functionallitys
int main(int argv, char* argc[]) {

	FunctionValues object = FunctionValues("testfile.txt");
	object.printValues();
	printf("[Main] Max values of object = %f\n", object.getMax());
	object.findSine();

	return 0;
}
