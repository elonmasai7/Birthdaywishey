import datetime

def calculate_birthday(name, birth_year):
  """Calculates the user's birthday and suggests a place to host the party.

  Args:
    name: The user's name, as a string.
    birth_year: The year the user was born, as an integer.

  Returns:
    A string containing the user's birthday, the number of months and days until
    the birthday, and a suggestion for a place to host the party.
  """

  # Get the current date and time.
  now = datetime.datetime.now()

  # Calculate the user's birthday.
  birthday = datetime.datetime(birth_year, now.month, now.day)

  # Calculate the number of months and days until the user's birthday.
  months_until_birthday = (birthday.year - now.year) * 12 + (birthday.month - now.month)
  days_until_birthday = birthday.day - now.day
  if days_until_birthday < 0:
    months_until_birthday -= 1
    days_until_birthday += 30

  # Suggest a place to host the user's birthday party.
  if months_until_birthday >= 6:
    place_to_host = "a park or outdoor venue"
  elif months_until_birthday >= 3:
    place_to_host = "a restaurant or event space"
  else:
    place_to_host = "your home or a local coffee shop"

  # Return the birthday, months and days until the birthday, and the place to host
  # the party.
  return f"Hi {name}, your birthday is on {birthday.strftime('%B %d, %Y')}. That's {months_until_birthday} months and {days_until_birthday} days away. You should consider hosting your party at {place_to_host}."


# Get the user's name and birth year.
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

# Calculate the user's birthday and suggest a place to host the party.
birthday_info = calculate_birthday(name, birth_year)

# Print the birthday information.
print(birthday_info)