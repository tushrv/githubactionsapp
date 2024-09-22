def add(*numbers):
  """
  This function takes any number of integer arguments and returns their sum.

  Args:
      *numbers (int, optional): Any number of integer arguments. Defaults to an empty tuple.

  Returns:
      int: The sum of all the provided arguments, or 0 if no arguments are provided.

  Raises:
      TypeError: If any non-integer argument is provided.
  """
  total = 0
  for num in numbers:
    if not isinstance(num, int):
      raise TypeError("Only integer arguments are allowed.")
    total += num
  return total