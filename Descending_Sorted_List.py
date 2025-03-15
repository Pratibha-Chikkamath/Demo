def second_largest_desc(lst):
    if len(lst) < 2:
        return "List must have at least two elements"

    return lst[1]  # Second element in descending order


# Example usage
lst = [99, 45, 20, 10, 4]  # Descending sorted list
print("Second largest element:", second_largest_desc(lst))
