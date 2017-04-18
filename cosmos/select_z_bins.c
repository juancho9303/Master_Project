#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 133358
//#define N 1182108   // For the whole sample (not the matched one)
//#define AR_c 150.5	
//#define DEC_c 2.2
//#define radius 0.01 //Twice the einstein radius in degrees

int main (void)
{
  int i;
  double alpha[N], delta[N], n[N], mu[N], z[N], z1, z2, z3, z4, z5, z6, z7, dis[N], b1, b2, b3, b4, b5, b6;
  
  z1 = 0.054;  z2 = 0.2; z3 = 0.4; z4 = 0.6; z5 = 0.8; z6 = 1.0; z7=1.2;
  
  FILE *data, *bins;
  data = fopen("data_R_matched.dat", "r");
//  data = fopen("data_R_whole.dat", "r"); 
  bins = fopen("zbins_matched.dat" , "w");
//  bins = fopen("zbins_whole.dat" , "w");
  
  for(i=0; i<N; i++)
    {  
      fscanf(data, "%lf\t %lf\t %lf\t %lf\t %lf\n", &alpha[i], &delta[i], &n[i], &mu[i], &z[i]);    
      //dis[i] = (sqrt(pow((alpha[i]-AR_c),2) + pow((delta[i]-DEC_c),2))); 
      //printf("%lf\n",dis[i]);
      if (23.0 > mu[i])
	{
	  //if (dis[i] < radius)
	    //{ 
	      if ( z1 < z[i] && z[i] < z2 ) 
		b1++;
	      if ( z2 < z[i] && z[i] < z3 )
		b2++;
	      if ( z3 < z[i] && z[i] < z4 )
		b3++;
	      if ( z4 < z[i] && z[i] < z5 )
		b4++;
	      if ( z5 < z[i] && z[i] < z6 )
		b5++;
		  if ( z6 < z[i] && z[i] < z7 )
		b6++;
	    //}
	}
    }
  printf(" %f-%f: %f\n %f-%f: %f\n %f-%f: %f\n %f-%f: %f\n %f-%f: %f\n %f-%f: %f\n", z1, z2, b1, z2, z3, b2, z3, z4, b3, z4, z5, b4, z5, z6, b5, z6, z7, b6);
  printf(" %f-%f: %f per arcmin\n %f-%f: %f per arcmin\n %f-%f: %f per arcmin\n %f-%f: %f per arcmin\n %f-%f: %f per arcmin\n %f-%f: %f per arcmin\n", z1, z2, b1/3600, z2, z3, b2/3600, z3, z4, b3/3600, z4, z5, b4/3600, z5, z6, b5/3600, z6, z7, b6/3600);
  fprintf(bins, " %f\t %f\n %f\t %f\n %f\t %f\n %f\t %f\n %f\t %f\n %f\t %f\n", (z1+z2)/2, b1/3600, (z2+z3)/2, b2/3600, (z3+z4)/2, b3/3600, (z4+z5)/2, b4/3600, (z5+z6)/2, b5/3600, (z6+z7)/2, b6/3600);
  fclose(data);
  fclose(bins); 
  
}
