#ifndef FINDSINE_H_
#define FINDSINE_H_

class FunctionValues {
 private:
	 int numValues;
	 double* values;
	 double y_delta;
	 double sineFreq;
	 double eqs; // error square sum
 public:
	 // Constructor, that reads values from a given file
	 FunctionValues(const char* argv);

	 // Deconstructor
	 ~FunctionValues();

	 // Prints all values of the class instance
	 void printValues();

	 // write values into a file
	 void writeValues(const char* argv);

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

	 // retruns sineFreq
	 double getSineFreq();

	 // retruns the error square sum (eqs) to generated sine
	 double getEQS();

	 // Finds a sine-function, that matches the values of the
	 // object and returns the factor to generate the sine
	 double findSine();

	 // Finds a cosine-function, that macthes the vlaues of the
	 // object and retruns the factor to generate the cosine
	 double findCosine();
};

// Generates a Sine with given parameters and saves the values
// in argv in the current directory
void genSine(double amp, double freq, int numValues,
		double c, const char* argv);

// Generates a Cosine with given parameters and saves the values
// in argv in the current directory
void genCosine(double amp, double freq, int numValues,
		double c, const char* argv);

#endif //_FINDSINE_H_
