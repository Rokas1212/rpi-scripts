#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<unistd.h>
int main() {
	FILE *fptr;

	//Store contents
	char buffer[16];
	int temperature;
	
	while(true) {
		//Open in read mode
		fptr = fopen("/sys/class/thermal/thermal_zone0/temp", "r");

		if(fptr != NULL) {
			while(fgets(buffer, sizeof(buffer), fptr) != NULL){
				temperature = atoi(buffer);
				temperature = temperature / 1000;
				printf("CPU Temp: %dC\n", temperature);
				fflush(stdout);
			}
		}
		//Close file
		fclose(fptr);

		sleep(1);
	}

	return 0;
}
