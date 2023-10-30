#include "lists.h"

/**
 *check_cycle - Function that checks if a singly linked list
 *              has a cycle
 *
 *@list: The singly linked list
 *Return: 0 if there is no cycle, 1 if there is one
 */

int check_cycle(listint_t *list)
{
	listint_t *lazy_ptr = list;
	listint_t *quick_ptr = list;
	int cycle = 0;

	while ((lazy_ptr && quick_ptr) && quick_ptr->next)
	{
		lazy_ptr = lazy_ptr->next;

		if (quick_ptr->next || quick_ptr->next->next)
			quick_ptr = quick_ptr->next->next;
		else
			break;

		if (lazy_ptr == quick_ptr)
		{
			cycle = 1;
			break;
		}
	}

	return (cycle);
}
