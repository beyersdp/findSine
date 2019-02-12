#ifndef FINDSINE_H_
#define FINDSINE_H_

#include <string>

class FunctionValues {
 private:
	 int numValues;
	 double* values;
	 double y_delta;
 public:
	 // Constructor, that reads values from a given file
	 FunctionValues(const char* argc);

	 // Deconstructor
	 ~FunctionValues();

	 // Prints all values of the class instance
	 void printValues();

	 // write values into a file
	 void writeValues(const char* argc);

 	 // Returns the max values ( = amplitude)
	 double getMax();

	 // Returns the number of values
	 int getNumValues();

	 // Normalizes all values to start with 0 (= y_delta)
	 void normalize();

	 // Add or subtract y_delta on each value
	 void denormalize();

	 // returns y_delta
	 double getY_Delta();

	 // Finds a sine-function, that matches the values of the
	 // object and returns the factor to generate the sine
	 double findSine();
};

// Generates a Sine with given parameters and saves the values
// in sine.txt in the current directory
void genSine(double amp, double freq, int numValues);

#endif //_FINDSINE_H_
