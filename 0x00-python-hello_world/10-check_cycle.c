#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - scan for cycles in linked lists
 * @list: pointer to head
 * Return: if cycle exists return 1 and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *clone = list;

	while (list)
	{
		if (!list->next)
			break;
		list = list->next->next;
		clone = clone->next;
		if (clone == list)
			return (1);
	}

	return (0);
}
