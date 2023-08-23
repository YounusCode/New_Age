def happy_birthday(name, year_born, current_year):
    new_age = current_year - year_born
    suffix = "th"
    if new_age % 10 == 1 and new_age % 100 != 11:
        suffix = "st"
    elif new_age % 10 == 2 and new_age % 100 != 12:
        suffix = "nd"
    elif new_age % 10 == 3 and new_age % 100 != 13:
        suffix = "rd"
    print(f"Happy {new_age}{suffix} Birthday, {name}!")


# Example of calling the function
happy_birthday('Emily', 1906, 1944)
