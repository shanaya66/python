# Display current date and time, and calendar info

import calendar
from datetime import datetime

# Get current date and time
current_time = datetime.now()

# Print current date and time
print("The current date and time is:", current_time)

# Print the full calendar for the year 2025
print(calendar.calendar(2025))

# Print the calendar for May 2025
print(calendar.month(2025, 5))
