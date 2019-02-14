# findSine
Project to fine a corresponding sine function for a given value series.

Based on the approche to analyze the results of an research experiment, this code projetc presents a soultion to generate automatically specific statistic values to valid the performance of a series of participant.

The following workflow should be implemented:
- Read the values from differents trys of multiple participants (three dimensions of correspondig values)
- Find fitting sine and cosine functions for the presented trends of numbers
- Calculate the error square sum for each number - (sine or cosine) pair
- Save the results with the original data for further computations

The developed code project is dividable in two essencial parts:
- Preprocess the data for each try of all participants [Python]
- Compute the required results on the organized data [C/C++]

This workflow should be exetuced automatically by a superordinated Python script

