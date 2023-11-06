#include "lists.h"

/**
 *is_palindrome - Checks if a singly linked list is a palindrome
 *
 *@head: Pointer to a pointer to the head of the linked list
 *
 *Return: If the linked list is not a palindrome - 0
 *        else 1 meaning the list is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *mid_node;
	size_t size = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (x = 0; x < (size / 2) - 1; x++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reverse = list_rev(&temp);
	mid_node = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	list_rev(&mid_node);

	return (1);
}

/**
 *list_rev - Reverses a singly-linked listint_t list
 *
 *@head: Pointer to pointer to the list to be reversed
 *
 *Return: pointer to the head of the reversed list
 */

listint_t *list_rev(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next, *pre = NULL;

	while (current)
	{
		next = current->next;
		current->next = pre;
		pre = current;
		current = next;
	}

	*head = pre;
	return (*head);
}
