DESDROID Inc. - Gradient Color Generation Module

This module provides functions for generating color gradients in Python.

**Features:**

* Create gradients between multiple colors.
* Specify colors in various formats (e.g., RGB, HEX, color names).
* Generate gradients with a specified amount of colors.

**Usage:**

```python
from gradify import Gradient

# Generate a linear gradient from cyan to blue to yellow with only an amount of 50 colors
length_of_gradient = 50
gradient_object:list = Gradient('cyan','blue','yellow')
gradient_colors = gradient_object.MindMultiGradient(
                        length_of_gradient
                        )
print(gradient_colors)

# there are still more, Explore
# Use the generated colors in your application...
#
#
#
```
