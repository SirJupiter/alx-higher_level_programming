#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked list
 * @h: head pointer pointing to first node of the list
 *
 * Return: number of elements
*/
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *temp;
	size_t count = 0;

	temp = h;

	if (!h)
		return (0);

	if (temp->prev)
		temp = temp->prev;

	while (temp)
	{
		count++;
		temp = temp->next;
	}

	return (count);
}
