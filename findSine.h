#ifndef FINDSINE_H_
#define FINDSINE_H_

#include <string>

class FunctionValues {
 private:
	 int numValues;
	 double* values;
 public:
	 // Constructor, that reads values from a given file
	 FunctionValues(int argv, const char* argc);

	 // Prints all values of the class instance
	 void printValues();
};

#endif //_FINDSINE_H_
