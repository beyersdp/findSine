#include <stdio.h>
#include <string.h>
#include "findSine.h"

// main function of the project to execute given functionallitys
int main(int argv, char* argc[]) {

	FunctionValues object = FunctionValues("realData.txt");
	object.normalize();
	printf("[Main] y_delta = %f\n", object.getY_Delta());
	object.printValues();
	object.writeValues("realData2.txt");
	object.findSine();
	
	printf("[Main] max Value = %f\n", object.getMax());

	genSine(object.getMax()*(-1), -0.032, object.getNumValues());

	return 0;
}
