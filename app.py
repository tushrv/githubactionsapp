def add(*numbers):
  """
  This function takes any number of arguments and returns their sum.

  Args:
      *numbers (int): Any number of integer arguments.

  Returns:
      int: The sum of all the provided arguments.
  """
  total = 0
  for num in numbers:
    if not isinstance(num, int):
      raise TypeError("Only integer arguments are allowed.")
    total += num
  return total

# Example usage (uncomment for testing purposes)
# print(add(2, 3))  # Output: 5
# print(add(1, 2, 3, 4))  # Output: 10