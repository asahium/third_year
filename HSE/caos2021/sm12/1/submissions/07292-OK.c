#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    if (argc <= 3) {
        exit(1);
    }
    pid_t pid = fork();
    if (!pid) {
        int in_fd = open(argv[2], O_RDONLY);
        int out_fd = open(argv[3], O_WRONLY | O_CREAT | O_TRUNC, 0666);
        dup2(in_fd, STDIN_FILENO);
        dup2(out_fd, STDOUT_FILENO);
        close(out_fd);
        close(in_fd);
        execlp(argv[1], argv[1], NULL);
        exit(1);
    }
    wait(NULL);
}
