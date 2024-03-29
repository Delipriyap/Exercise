#include<stdio.h>
   #include<signal.h>
   #include<stdlib.h>
 
   int main()
   {
       pid_t child;
       child=fork();
       switch(child){
           case -1 :
               perror("fork");
               exit(1);
           case 0 :
               while(1){
                   printf("Child Process\n");
                   sleep(1);
               }
               break;              
           default :
               sleep(5);
               kill(child,SIGINT);
               printf("The child process has been killed by the parent process\n");
               break;
       }
       return 0; 
 }

