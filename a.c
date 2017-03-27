#include <stdio.h>
#include <string.h>

int main(){
  char a[1024] = "Hello how are you";
  char *b = "Appending this";
  char *c = "Appending that";


  strcat(a,b);
  strcat(a,c);

  printf("%s",a);


  return 0;
}
