#include <stdio.h>
#include <unistd.h>
#include <unistd.h>

/**
 * infinite_while - not main
 * Return: 0
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
 * main - main
 * Return: 0
 */
int main(void)
{
	pid_t DontDeadOpenInside;
	int i;

	for (i = 0; i < 5; i++)
	{
		DontDeadOpenInside = fork();
		if (!DontDeadOpenInside)
			return (0);
		printf("Zombie process created, PID: %d\n", DontDeadOpenInside);
	}
	return (infinite_while());
}
