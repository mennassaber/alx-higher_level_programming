#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int array[1000]; // Assuming the maximum size of the linked list is 1000
    int i = 0, j;

    // Store the values of the linked list in an array
    while (current != NULL)
    {
        array[i] = current->n;
        current = current->next;
        i++;
    }
    // Initialize pointers for array comparison
    i--; // Move i to the last index of the array
    j = 0; // Start j from the first index
    // Compare elements from the beginning and end of the array
    while (j < i)
    {
        if (array[j] != array[i])
            return 0; // Not a palindrome
        j++;
        i--;
    }
    return 1; // Palindrome
}
