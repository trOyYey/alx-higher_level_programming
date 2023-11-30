#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts number into sorted singly linked list
 * @head: pointer to pointer of first node of linked list
 * @number: integer to be added to the list
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_clone, *tmp_clone;

	if (!head)
		return (NULL);
	tmp_clone = *head;

	new_clone = malloc(sizeof(listint_t));
	if (!new_clone)
		return (new_clone);

	new_clone->n = number;

	if (*head == NULL || tmp_clone->n >= number)
	{
		new_clone->next = *head;
		*head = new_clone;
	}
	else
	{
		while (tmp_clone->next != NULL && tmp_clone->next->n < number)
			tmp_clone = tmp_clone->next;
		new_clone->next = tmp_clone->next;
		tmp_clone->next = new_clone;
	}

	return (new_clone);
}
