import numpy as np

def get_line_coordinates(start_x, start_y, end_x, end_y):
  """
  This function generates a list of coordinates representing a line segment
  from a starting point (start_x, start_y) to an ending point (end_x, end_y).

  Args:
      start_x: X-coordinate of the starting point.
      start_y: Y-coordinate of the starting point.
      end_x: X-coordinate of the ending point.
      end_y: Y-coordinate of the ending point.

  Returns:
      A list of tuples representing the (x, y) coordinates of the line segment.
  """

  # Calculate the change in x and y
  delta_x = end_x - start_x
  delta_y = end_y - start_y

  # Handle potential division by zero (straight line)
  if delta_x == 0:
    # Create a list of points with the same x-coordinate
    return [(start_x, y) for y in range(start_y, end_y + 1)]
  elif delta_y == 0:
    # Create a list of points with the same y-coordinate
    return [(x, start_y) for x in range(start_x, end_x + 1)]

  # Calculate the slope
  slope = delta_y / delta_x

  # Generate a list of x values from start_x to end_x
  x_vals = np.linspace(start_x, end_x, num=max(abs(delta_x), abs(delta_y)) + 1, dtype=int)

  # Calculate the corresponding y values using the slope
  y_vals = slope * (x_vals - start_x) + start_y

  # Combine x and y values into a list of coordinates
  coordinates = list(zip(x_vals, y_vals))

  return coordinates

# Example usage
start_x = 100
start_y = 100
end_x = 400
end_y = 50

line_coordinates = get_line_coordinates(start_x, start_y, end_x, end_y)

print(line_coordinates)
