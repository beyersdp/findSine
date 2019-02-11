#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "findSine.h"

//____________________________________________________________________
FunctionValues::FunctionValues(const char* argc) {
	
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
	printf("%s\n", line);
	printf("[FunctionValues] Reading value: %f\n", atof(line));
	numValues++;
	}
	
	// close file stream to reset the pointer for next iteration
	fclose(fp);
	
	// alloc memory for saving all numbers in the file
	printf("[FunctionValues] %d values found\n", numValues);
	this->numValues = numValues;
	this->values = new double[numValues];
	this->y_delta = 0;

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
FunctionValues::~FunctionValues() {
	delete this->values;
}

//___________________________________________________________________
void FunctionValues::printValues() {
	
	for(int i = 0; i < this->numValues; i++) {
		printf("[printValues] %f\n", this->values[i]);
	}
}

//___________________________________________________________________
void FunctionValues::writeValues(const char* argc) {
	
	FILE* fp = fopen(argc, "w");
	if (fp == NULL) {
		printf("[writeValues][ERR] Cannot create file\n");
		exit(1);
	}

	for (int i = 0; i < this->numValues; i++) {
		fprintf(fp, "%f\n", this->values[i]);
		printf("[writeValues] %f written\n", this->values[i]);	      }

	fclose(fp);
}

//___________________________________________________________________
int FunctionValues::getNumValues() {
	return this->numValues;
}

//___________________________________________________________________
double FunctionValues::getMax() {

	double maxValue = 0;
	double minValue = 0;
	for (int i = 0; i < this->numValues; i++) {
		if (this->values[i] > maxValue) {
			maxValue = this->values[i];
		}
		if (this->values[i] < minValue) {
			minValue = this->values[i];
		}
	}

	if (((-2) * minValue) > maxValue) {
		return minValue;
	}
	else {
		return maxValue;
	}
}

//___________________________________________________________________
void FunctionValues::normalize() {
	
	this->y_delta = this->values[0];

	if (this->y_delta > 0) {
		for (int i = 0; i < this->numValues; i++) {
			this->values[i] -= y_delta;
		}
	}

	if (this->y_delta < 0) {
		for (int j = 0; j < this->numValues; j++) {
			this->values[j] += y_delta;
		}
	}
}

//___________________________________________________________________
double FunctionValues::getY_Delta() {

	return this->y_delta;
}

//___________________________________________________________________
double FunctionValues::findSine() {
	
	double bestFreq = 0.0;
	int bestMatches = 0;

	int matches = 0;
	double amp = this->getMax();

	if (amp < 0) {
		amp = amp * (-1);
	}

	for (double i = -0.01; i > -1; i -= 0.001) {
		printf("[findSine][%f]", i);
		for (int j = 0; j < this->numValues; j++) {
		
			/*if ((amp * sin(i*j)) == this->values[j]) {
				matches++;
			}*/
			double diff = this->values[j]-(amp*sin(i*j));
		if (abs(diff) < 0.09) {
			matches++;
			}

		if (matches > bestMatches) {
			bestMatches = matches;
			bestFreq = i;
		}
		}
		matches = 0;
		printf(" best matches = %d\n", bestMatches);	
	}

	printf("[findSine] best matches (%d) with %f\n",
			bestMatches, bestFreq);

	return bestFreq;
}

//___________________________________________________________________
void genSine(double amp, double freq, int numValues) {

	FILE* fp = fopen("sine.txt", "w");
	if (fp == NULL) {
		printf("[genSine][ERR] Cannot create file\n");
		exit(1);
	}

	double value = 0;
	for (int i = 0; i < numValues; i++) {
		value = amp * sin(freq * i);
		printf("[genSine][%d] %f\n",i, value);
		fprintf(fp, "%f\n", value);	
	}

	fclose(fp);
}



