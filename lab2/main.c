#include <stdio.h>
#include <string.h>

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

int my_printf(char *format_string, char *param){
	for(int i=0;i<strlen(format_string);i++){
		if((format_string[i] == '#') && (format_string[i+1] == 'k')){
			i++;
			printf("%s",param);
		}else
			putchar(format_string[i]);
	}
	puts("");
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}
