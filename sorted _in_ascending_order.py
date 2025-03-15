def second_largest_sorted(lst):
    if len(lst) < 2:
        return "List must have at least two elements"

    return lst[-2]  # Second last element in a sorted list


# Example usage
lst = [1, 3, 5, 7, 9]  # Sorted list
print("Second largest element:", second_largest_sorted(lst))
