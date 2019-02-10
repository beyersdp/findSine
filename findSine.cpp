#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "findSine.h"

//____________________________________________________________________
FunctionValues::FunctionValues(int argv, const char* argc) {
	
	// open given file in dir by name in reading mode
	FILE* fp = fopen(argc, "r");
	if (fp == NULL) {
		printf("[FunctionValues][ERR] Cannot open file\n");
		return;
	}

	// read open file line by line and count the values
	char* line = NULL;
	size_t len = 0;
	numValues = 0;
	while ((getline(&line, &len, fp)) != -1) {
	printf("[FunctionValues] Reading value: %f\n", atof(line));
	numValues++;
	}
	
	// close file stream to reset the pointer for next iteration
	fclose(fp);
	
	// alloc memory for saving all numbers in the file
	printf("[FunctionValues] %d values found\n", numValues);
	this->numValues = numValues;
	this->values = new double[numValues];
	
	// open given file again in reading mode
	fp = fopen(argc, "r");
	if (fp == NULL) {
		printf("[FunctionValues][ERR] Cannot open file\n");
		return;
	}
	
	// write all values from the file in the memory of the object
	line = NULL;
	len = 0;
	int i = 0;
	while((getline(&line, &len, fp)) != -1) {
		this->values[i] = atof(line);
		i++;
	}

	fclose(fp);
}

//___________________________________________________________________
void FunctionValues::printValues() {
	
	for(int i = 0; i < this->numValues; i++) {
		printf("[printValues] %f\n", this->values[i]);
	}
}
