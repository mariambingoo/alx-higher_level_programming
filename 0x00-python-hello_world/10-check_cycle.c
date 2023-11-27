#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - cycle checker
 * list: list to detect
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
