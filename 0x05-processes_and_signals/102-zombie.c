#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - hangs the process
 *Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 *main - create and show processes
 *Return: Success or failure
 */

int main(void)
{
	pid_t p;
	int process = 0;

	while (process < 5)
	{
		p = fork();
		if (p < 0)
		{
			perror("Fork failed");
			exit(1);
		}
		else if (p > 0)
		{
			printf("Zombie process created, PID: %d\n", p);
			sleep(1);
			process++;
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}
