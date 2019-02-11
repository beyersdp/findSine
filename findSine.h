#ifndef FINDSINE_H_
#define FINDSINE_H_

#include <string>

class FunctionValues {
 private:
	 int numValues;
	 double* values;
 public:
	 // Constructor, that reads values from a given file
	 FunctionValues(const char* argc);

	 // Prints all values of the class instance
	 void printValues();

	 // TODO: writeValues(const char* argc) into a file
	
 	 // Returns the max values ( = amplitude)
	 double getMax();

	 // Finds a sine-function, that matches the values of the
	 // object and returns the factor to generate the sine
	 double findSine();
};

// 
void genSine(double amp, double freq, int numValues);
//TODO: retruns a FunctionValues object

#endif //_FINDSINE_H_
