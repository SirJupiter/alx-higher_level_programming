#include "lists.h"

/**
 * check_cycle - checks if linked list contains a cycle
 * @list: pointer to list
 *
 * Return: 0 if no cycle; 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *one_list, *two_list;

	one_list = list;
	two_list = list;

	if (list == NULL)
		return (0);

	while (one_list && two_list && two_list->next)
	{
		one_list = one_list->next;
		two_list = two_list->next->next;
		if (one_list == two_list)
			return (1);
	}

	return (0);
}
