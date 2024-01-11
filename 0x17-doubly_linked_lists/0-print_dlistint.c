#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: head pointer pointing to the first node
 *
 * Return: number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *temp;
	size_t count = 0;

	if (h == NULL)
		return (count);

	temp = h;

	while (temp->prev != NULL)
		temp = temp->prev;

	while (temp != NULL)
	{
		printf("%d\n", temp->n);
		count++;
		temp = temp->next;
	}

	return (count);
}
