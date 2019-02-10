all: findSineMain clean

findSineMain: findSineMain.o findSine.o
	g++ -o findSineMain findSineMain.o findSine.o

findSineMain.o: findSineMain.cpp
	g++ -c findSineMain.cpp

findSine.o: findSine.cpp
	g++ -c findSine.cpp

clean:
	rm -f *.o
