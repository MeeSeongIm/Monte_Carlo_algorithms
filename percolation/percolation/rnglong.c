// percolation sample that corresponds to the paper:
// http://www.santafe.edu/media/workingpapers/01-02-010.pdf


#include <time.h>

/* Constants */

#define A 2416
#define C 374441
#define M 1771875
#define CONV 2423.96743336861

/* Globals */

unsigned long int i;
unsigned long int rng_ia[1279];
int rng_p,rng_pp;
int rng_mod[1279];


/* Function to seed the random number generator.  If the seed given is
 * zero, then the RNG is seeded from the clock */

void rngseed(unsigned long int s)
{
  int n;

  /* If seed is zero, set it from the clock */

  if (s==0) s = time(0);

  /* First seed the linear congruential generator */

  i = s;

  /* Use that to seed the additive generator.  Also set up the mod array */

  for (n=0; n<1279; n++) {
    rng_ia[n] = CONV*(i=(A*i+C)%M);
    rng_mod[n] = n-1;
  }
  rng_mod[0] = 54;

  rng_p = 0;
  rng_pp = 418;

  /* Run off a million random numbers, just to get things started */

  for (n=0; n<1000000; n++)
    rng_ia[rng_p=rng_mod[rng_p]] += rng_ia[rng_pp=rng_mod[rng_pp]];
}



