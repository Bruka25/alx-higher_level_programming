#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 *insert_node - inserts a number into a sorted singly linked list
 *
 *@head: Pointer to a pointer to the head of the list
 *@number: Number to be inserted
 *
 *Return: Address of a new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = NULL, *latest_node = NULL, *buff = NULL;

	latest_node = malloc(sizeof(listint_t));
	if (latest_node == NULL)
		return (NULL);

	latest_node->n = number;
	if (*head)
	{
		current_node = *head;
		if (number <= current_node->n)
		{
			latest_node->next = current_node;
			*head = latest_node;
		}
		else
		{
			while (current_node->next)
			{
				if (number <= current_node->next->n)
				{
					buff = current_node->next;
					current_node->next = latest_node;
					latest_node->next = buff;
					return (*head);
				}

				current_node = current_node->next;
			}
			buff = current_node->next;
			current_node->next = latest_node;
			latest_node->next = buff;
		}
		return (*head);
	}
	latest_node->next = NULL;
	*head = latest_node;
	return (*head);
}
