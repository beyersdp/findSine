#include <stdio.h>
#include <string.h>
#include "findSine.h"

// main function of the project to execute given functionallitys
int main(int argc, char* argv[]) {

	FunctionValues object = FunctionValues(argv[1]);
	object.normalize();
	printf("[Main] y_delta = %f\n", object.getY_Delta());
	printf("[Main] max Value = %f\n", object.getMax());	

	if (!strcmp(argv[4], "sin")) {
		double freq = object.findSine();
	
		printf("[Main] amp = %f freq= %f c = %f\n"
			, object.getMax(), freq, object.getY_Delta());
		printf("[Main] y = %f * sin(%f * x) + (%f)\n"
			, object.getMax(), freq, object.getY_Delta());

		genSine(object.getMax(), freq, object.getNumValues(),
				object.getY_Delta(), argv[2]);

		FILE* fp = fopen(argv[3], "w");
		fprintf(fp, "y = %f * sin(%f * x) + (%f)\n"
			, object.getMax(), freq, object.getY_Delta());
		fprintf(fp, "%f\n", object.getEQS());
		fclose(fp);
	}

	if (!strcmp(argv[4], "cos")) {
		double freq = object.findCosine();
	
		printf("[Main] amp = %f freq= %f c = %f\n"
			, (object.getMax()/2), freq
			, (-(object.getMax()/2)+object.getY_Delta()));
		printf("[Main] y = %f * cos(%f * x) + (%f)\n"
			, (object.getMax()/2), freq
			, (-(object.getMax()/2)+object.getY_Delta()));

		genCosine(object.getMax(), freq, object.getNumValues()
			, object.getY_Delta(), argv[2]);

		FILE* fp = fopen(argv[3], "w");
		fprintf(fp, "y = %f * cos(%f * x) + (%f)\n"
			, (object.getMax()/2), freq
			, (-(object.getMax()/2)+object.getY_Delta()));
		fprintf(fp, "%f\n", object.getEQS());
		fclose(fp);
	}

	return 0;
}
