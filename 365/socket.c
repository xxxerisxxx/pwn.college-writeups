#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int pwncollege(){//int argc, char *argv[]) {
        int socket_desc;
        struct sockaddr_in server;
        char *message, server_reply[20000];

        socket_desc = socket(AF_INET, SOCK_STREAM, 0);
        if (socket_desc == -1) {
                printf("failed");
        }

        server.sin_addr.s_addr = inet_addr("127.0.0.1");
        server.sin_family = AF_INET;
        server.sin_port = htons(1857);

        if (connect(socket_desc, (struct sockaddr *)&server, sizeof(server))<0) {
                puts("error");
                return 1;
        }

        puts("Connected");
        //while (socket_desc!=-1) {

                if (recv(socket_desc, server_reply, 20000, 0)<0) {
                        puts("recv failed");
                }
                puts("Reply received");
                while (socket_desc>-1) {
                        puts(server_reply);
                        read(socket_desc, server_reply, 20000);
                }
                //close(socket_desc);
        //}
        return 0;
}

int main() {
        pwncollege();
        return 0;
}
