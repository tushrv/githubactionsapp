import pytest
import os
import sys

root = os.path.dirname(os.path.dirname(__file__))
sys.path.append("root")

import app
def test_add_with_zero_arguments():
  assert app.add() == 0  # Or raise an error if preferred

@pytest.mark.parametrize("numbers, expected_sum", [
  ([2, 3], 5),
  ([1, 2, 3, 4], 10),
  ([-2, 5], 3),
  ([], 0),  # Or raise an error if preferred
])
def test_add_various_inputs(numbers, expected_sum):
  assert app.add(*numbers) == expected_sum

def test_add_non_integers():
  with pytest.raises(TypeError):
    app.add(2, "hello")