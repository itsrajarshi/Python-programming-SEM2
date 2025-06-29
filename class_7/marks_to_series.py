import numpy as np
import pandas as pd

# Create NumPy array of marks
marks = np.array([34, 56, 78, 90, 89])

# Convert to pandas Series with subject names
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
marks_series = pd.Series(marks, index=subjects)

# Display the Series
print("Marks in Each Subject:")
print(marks_series)