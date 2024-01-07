#include "lists.h"
#include <stdio.h>

/**
 * move - move pointer to position and fill a comparison array
 * @len: length
 * @forward: pointer
 * @array: array to fill up
 */

void move(int len, listint_t **forward, int (*array)[])
{
	int i;

	(*array)[0] = (*forward)->n;

	for (i = 1; i < (len / 2); i++)
	{
		*forward = (*forward)->next;
		(*array)[i] = (*forward)->n;
	}
	if (len % 2 == 0)
		*forward = (*forward)->next;
	else
		*forward = (*forward)->next->next;
}
/**
 * is_palindrome - Checks if a linkedlist is a palindrome
 * @head: entry point to the linkedlist
 *
 * Return: 0 if false, 1 if true
 */

int is_palindrome(listint_t **head)
{
	int array[1024];
	int len = 0, mid;
	listint_t *forward, *ptr;

	if (!head)
		return (0);
	if (!(*head) || (*head)->next == NULL)
		return (1);

	ptr = *head;

	while (ptr)
	{
		len += 1;
		ptr = ptr->next;
	}
	mid = len / 2;

	forward = *head;

	move(len, &forward, &array);

	while (mid > 0)
	{
		if (forward->n != array[mid - 1])
			return (0);
		mid--;
		forward = forward->next;
	}
	return (1);
}
