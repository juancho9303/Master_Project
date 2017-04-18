#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 133358

int main (void)
{
  int i;
  double idg[N], fluxg[N], flux_errg[N], xg[N], yg[N], magg[N], flux_radg[N];
  double idr[N], fluxr[N], flux_errr[N], xr[N], yr[N], magr[N], flux_radr[N];
  double idu[N], fluxu[N], flux_erru[N], xu[N], yu[N], magu[N], flux_radu[N];
  double idi[N], fluxi[N], flux_erri[N], xi[N], yi[N], magi[N], flux_radi[N];
  
  FILE *datag, *datar, *datau, *datai, *outg, *outr, *outu, *outi;
  datag = fopen("A754g.cat", "r"); datar = fopen("A754r.cat", "r"); datau = fopen("A754u.cat", "r"); datai = fopen("A754i.cat", "r");
  outg = fopen("filtered_flux_g.dat" , "w"); outr = fopen("filtered_flux_r.dat" , "w"); outu = fopen("filtered_flux_u.dat" , "w"); 
  outi = fopen("filtered_flux_i.dat" , "w");
  
  for(i=0; i<N; i++)
    {  
      fscanf(datag, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", &idg[i], &fluxg[i], &flux_errg[i], &xg[i], &yg[i], &magg[i], &flux_radg[i]);
      fscanf(datar, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", &idr[i], &fluxr[i], &flux_errr[i], &xr[i], &yr[i], &magr[i], &flux_radr[i]); 
      fscanf(datau, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", &idu[i], &fluxu[i], &flux_erru[i], &xu[i], &yu[i], &magu[i], &flux_radu[i]); 
      fscanf(datai, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", &idi[i], &fluxi[i], &flux_erri[i], &xi[i], &yi[i], &magi[i], &flux_radi[i]);   

	      if ( 23.3 < magr[i] && flux_radr[i] < 2.25 )
	      { 

/*	
y = mat1[:,1] #mag
z = mat1[:,6] #flux radius

filter1 = (mat1[:,1]<23.3)&(mat1[:,6]<2.25)
filter4 = (mat1[:,1]<18)&(mat1[:,6]<3.25)
filter5 = (mat1[:,1]<24)&(mat1[:,6]<2)
filter2 = (mat1[:,1]<16.0)
filter3 = (mat1[:,1]<30.0)
*/
	fprintf(datag, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", idg[i], fluxg[i], flux_errg[i], xg[i], yg[i], magg[i], flux_radg[i]);
	fprintf(datar, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", idr[i], fluxr[i], flux_errr[i], xr[i], yr[i], magr[i], flux_radr[i]);
	fprintf(datau, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", idu[i], fluxu[i], flux_erru[i], xu[i], yu[i], magu[i], flux_radu[i]);
	fprintf(datai, "%d\t %f\t %f\t %f\t %f\t %f\t %f\n", idi[i], fluxi[i], flux_erri[i], xi[i], yi[i], magi[i], flux_radi[i]);
    }
}

  fclose(datag); fclose(datar); fclose(datau); fclose(datai);
  fclose(outg); fclose(outr); fclose(outu); fclose(outi); 
  
}
