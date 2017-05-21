#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 414

int main (void)
{
  int i;
  float idg[N], fluxg[N], flux_errg[N], xg[N], yg[N], magg[N], flux_radg[N];
  float idr[N], fluxr[N], flux_errr[N], xr[N], yr[N], magr[N], flux_radr[N];
  float idu[N], fluxu[N], flux_erru[N], xu[N], yu[N], magu[N], flux_radu[N];
  float idi[N], fluxi[N], flux_erri[N], xi[N], yi[N], magi[N], flux_radi[N];
  
  FILE *datag, *datar, *datau, *datai, *outg, *outr, *outu, *outi;
  datag = fopen("A754g.cat", "r"); datar = fopen("A754r.cat", "r"); datau = fopen("A754u.cat", "r"); datai = fopen("A754i.cat", "r");
  outg = fopen("filtered_flux_g.dat" , "w"); outr = fopen("filtered_flux_r.dat" , "w"); outu = fopen("filtered_flux_u.dat" , "w"); 
  outi = fopen("filtered_flux_i.dat" , "w");
  
  for(i=0; i<N; i++)
    {  
      fscanf(datag, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", &idg[i], &fluxg[i], &flux_errg[i], &xg[i], &yg[i], &magg[i], &flux_radg[i]);
      fscanf(datar, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", &idr[i], &fluxr[i], &flux_errr[i], &xr[i], &yr[i], &magr[i], &flux_radr[i]); 
      fscanf(datau, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", &idu[i], &fluxu[i], &flux_erru[i], &xu[i], &yu[i], &magu[i], &flux_radu[i]); 
      fscanf(datai, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", &idi[i], &fluxi[i], &flux_erri[i], &xi[i], &yi[i], &magi[i], &flux_radi[i]);   
      
      if ( magr[i] > 17 )
	{ 
	  if(flux_radr[i] > 2.44 )
	    {
	      fprintf(outg, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idg[i], fluxg[i], flux_errg[i], xg[i], yg[i], magg[i], flux_radg[i]);
	      fprintf(outr, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idr[i], fluxr[i], flux_errr[i], xr[i], yr[i], magr[i], flux_radr[i]);
	      fprintf(outu, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idu[i], fluxu[i], flux_erru[i], xu[i], yu[i], magu[i], flux_radu[i]);
	      fprintf(outi, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idi[i], fluxi[i], flux_erri[i], xi[i], yi[i], magi[i], flux_radi[i]);
	    }
	}
	
	if ( magr[i] > 24 )
	{ 
	  if(flux_radr[i] < 2.24 )
	    {
	      fprintf(outg, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idg[i], fluxg[i], flux_errg[i], xg[i], yg[i], magg[i], flux_radg[i]);
	      fprintf(outr, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idr[i], fluxr[i], flux_errr[i], xr[i], yr[i], magr[i], flux_radr[i]);
	      fprintf(outu, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idu[i], fluxu[i], flux_erru[i], xu[i], yu[i], magu[i], flux_radu[i]);
	      fprintf(outi, "%f\t %f\t %f\t %f\t %f\t %f\t %f\n", idi[i], fluxi[i], flux_erri[i], xi[i], yi[i], magi[i], flux_radi[i]);
	    }
	}
    }
  
  fclose(datag); fclose(datar); fclose(datau); fclose(datai);
  fclose(outg); fclose(outr); fclose(outu); fclose(outi); 
  
}
