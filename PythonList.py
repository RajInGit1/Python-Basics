# # Create a List
# # Write a Python program to create a list of five integers and print the list.
# List = [12,13,14,15,16]
# print(List)
# type(List)


# # Access List Elements

# numbers = [10, 20, 30, 40, 50]

# print("First element:", numbers[0])
# print("Third element:", numbers[2])
# print("Last element:", numbers[-1])

# # Write a program to display the first, last, and third elements of a list.

# numbers = [10, 20, 30]

# numbers.append(40)      # Add at the end
# numbers.insert(1, 15)   # Add at index 1

# print(numbers)


# # Add Elements


# numbers = [10, 20, 30, 40, 50]

# print("First element:", numbers[0])
# print("Third element:", numbers[2])
# print("Last element:", numbers[-1])

# # Write a program to add a new element at the end of a list and at a specific position.


# # Remove Elements
# # Write a program to remove an element from a list by value and by index.
# # Find the Largest Element
# # Write a program to find the largest number in a list without using the max() function.
# # Find the Smallest Element
# # Write a program to find the smallest number in a list without using the min() function.
# # Calculate the Sum
# # Write a program to calculate the sum of all elements in a list.
# # Count Even and Odd Numbers
# # Write a program to count the number of even and odd numbers in a list.
# # Reverse a List
# # Write a program to reverse the elements of a list without using the reverse() method.
# # Remove Duplicates
# # Write a program to remove duplicate elements from a list while preserving the original order.
# # Search an Element
# # Write a program to check whether a given element exists in a list.
# # Sort a List
# # Write a program to sort a list in ascending and descending order.
# # Merge Two Lists
# # Write a program to combine two lists into a single list.
# # Find the Second Largest Element
# # Write a program to find the second largest element in a list.
# # Count Occurrences
# # Write a program to count how many times a specific element appears in a list.

# Below are Python solutions for all 15 list problems.

# ### 1. Create a List

# ```python
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# ```

# ---

# ### 2. Access List Elements

# ```python
# numbers = [10, 20, 30, 40, 50]

# print("First element:", numbers[0])
# print("Third element:", numbers[2])
# print("Last element:", numbers[-1])
# ```

# ---

# ### 3. Add Elements

# ```python
# numbers = [10, 20, 30]

# numbers.append(40)      # Add at the end
# numbers.insert(1, 15)   # Add at index 1

# print(numbers)
# ```

# ---

# ### 4. Remove Elements

# ```python
# numbers = [10, 20, 30, 40, 50]

# numbers.remove(30)   # Remove by value
# numbers.pop(1)       # Remove by index

# print(numbers)
# ```

# ---

# ### 5. Find the Largest Element (Without `max()`)

# ```python
# numbers = [10, 25, 8, 50, 15]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest element:", largest)
# ```

# ---

# ### 6. Find the Smallest Element (Without `min()`)

# ```python
# numbers = [10, 25, 8, 50, 15]

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# print("Smallest element:", smallest)
# ```

# ---

# ### 7. Calculate the Sum

# ```python
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for num in numbers:
#     total += num

# print("Sum:", total)
# ```

# ---

# ### 8. Count Even and Odd Numbers

# ```python
# numbers = [10, 21, 32, 45, 56, 67]

# even = 0
# odd = 0

# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even)
# print("Odd:", odd)
# ```

# ---

# ### 9. Reverse a List (Without `reverse()`)

# ```python
# numbers = [10, 20, 30, 40, 50]

# reversed_list = []

# for i in range(len(numbers) - 1, -1, -1):
#     reversed_list.append(numbers[i])

# print(reversed_list)
# ```

# ---

# ### 10. Remove Duplicates

# ```python
# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print(unique)
# ```

# ---

# ### 11. Search an Element

# ```python
# numbers = [10, 20, 30, 40, 50]

# search = 30

# if search in numbers:
#     print("Element found.")
# else:
#     print("Element not found.")
# ```

# ---

# ### 12. Sort a List

# ```python
# numbers = [50, 20, 10, 40, 30]

# ascending = sorted(numbers)
# descending = sorted(numbers, reverse=True)

# print("Ascending:", ascending)
# print("Descending:", descending)
# ```

# ---

# ### 13. Merge Two Lists

# ```python
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# merged = list1 + list2

# print(merged)
# ```

# ---

# ### 14. Find the Second Largest Element

# ```python
# numbers = [10, 50, 20, 40, 30]

# largest = second = float("-inf")

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif largest > num > second:
#         second = num

# print("Second Largest:", second)
# ```

# ---

# ### 15. Count Occurrences of an Element

# ```python
# numbers = [1, 2, 3, 2, 4, 2, 5]

# element = 2
# count = 0

# for num in numbers:
#     if num == element:
#         count += 1

# print(f"{element} appears {count} times.")
# ```

# These solutions are beginner-friendly and avoid using advanced concepts where possible, making them suitable for a **Python Basics** GitHub repository.
