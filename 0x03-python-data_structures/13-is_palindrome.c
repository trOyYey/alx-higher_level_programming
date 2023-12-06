#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome -  palindrome check.
 * @head: pointer to headlist
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	static int palin[1024];
	int z, y;
	listint_t *curr;

	if (!head || !*head)
		return (1);
	/* this loop to know the how many lists there is*/
	for (z = 0, curr = *head; curr != NULL; z++)
		curr = curr->next;
	/*this loop will traverse a cross the first half, as long as y <=z*/
	for (y = 0, z -= 1, curr = *head; curr != NULL; y++, z--)
	{
		if (y <= z)
			palin[y] = curr->n;
		/* when y > z it will start comparing between 2nd half and first half saved in pal */
		else if (palin[z] != curr->n)
			return (0);
		curr = curr->next;
	}
	return (1);
}
