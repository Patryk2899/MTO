#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void display(int size, char* param) {
	for (int j=0;j<size;j++){
		if (param[j] >= 65 && param[j] <= 90){
			printf("%c", param[j] + 32);
		}else if (param[j] >= 97 && param[j] <= 122 ){
			printf("%c", param[j] - 32);
		}else {
			printf("%c", param[j]);
		}
	}
}

void display_according_to_size(int size, char* param){
	int result;
	if(size > strlen(param)){
		result = size - strlen(param);
		for (int i = 0; i < result ; i++){
			printf(" ");
		}
		display(strlen(param), param);
	}else{
		display(size, param);
	}
}

int my_printf(char *format_string, char *param){
	int size = 0;
	int k = 0;
	int index = 0;
	char length[4];
	for(int i=0;i<strlen(format_string);i++){
		if((format_string[i] == '#') && (format_string[i+1] == '.')){
			if (format_string[i+2] >= 48 && format_string[i+2] <= 57){
				k = i+2;
				while (format_string[k] >= 48 && format_string[k] <= 57){
					length[index] = format_string[k];
					k++;
					index++;
				}
				if (format_string[k] == 'k'){
					size = atoi(length);
					if (size > strlen(param)){
						size = strlen(param);
					}
					display(size, param);
					i+=index+2;
				}else {
					putchar(format_string[i]);
					continue;
				}
			}else{
				putchar(format_string[i]);
				continue;
			}
		}else if(format_string[i] == '#' && (format_string[i+1] >= 48 && format_string[i+1] <= 57)){
			k = i+1;
				while (format_string[k] >= 48 && format_string[k] <= 57){
					length[index] = format_string[k];
					k++;
					index++;
				}
				if (format_string[k] == 'k'){
					size = atoi(length);
					display_according_to_size(size, param);
					i+=index+1;
				}else{
					putchar(format_string[i]);
					continue;
				}
		}
		else if ((format_string[i] == '#') && (format_string[i+1] == 'k')){
			display(strlen(param), param);
			i++;
		}
		else
			putchar(format_string[i]);
	}
	puts("");
	return 0;
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}
