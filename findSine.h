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
	
 	 // Returns the max values ( = amplitude)
	 double getMax();

	 // Finds a sine-function, that matches the values of the
	 // object and returns the factor to generate the sine
	 double findSine();
};

#endif //_FINDSINE_H_
