#include <stdio.h>
#include <string.h>
#include "findSine.h"

// main function of the project to execute given functionallitys
int main(int argv, char* argc[]) {

	FunctionValues object = FunctionValues(argc[1]);
	object.normalize();
	printf("[Main] y_delta = %f\n", object.getY_Delta());
	printf("[Main] max Value = %f\n", object.getMax());
	object.writeValues(argc[2]);
		
	double freq = object.findSine();
	
	printf("[Main] amp = %f freq= %f c = %f\n"
		, object.getMax(), freq, object.getY_Delta());
	
	genSine(object.getMax(), freq, object.getNumValues());

	return 0;
}
