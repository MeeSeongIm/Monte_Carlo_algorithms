// percolation sample that corresponds to the paper:
// http://www.santafe.edu/media/workingpapers/01-02-010.pdf


CFLAGS = -O6
CC = gcc
LIBS = -lm

perc:perc.o rnglong.o
	$(CC) $(CFLAGS) -o perc $(LIBS) perc.o rnglong.o

perc.o:perc.c rnglong.h Makefile
	$(CC) $(CFLAGS) -c perc.c

rnglong.o:rnglong.c rnglong.h Makefile
	$(CC) $(CFLAGS) -c rnglong.c

	
	
