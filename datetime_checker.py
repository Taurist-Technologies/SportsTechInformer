import datetime


# Converts a string to a date object
# compared the datetime attribute to today's date
# returns True if the date is today's date
def is_today_from_string(date_string: str) -> bool:
    if not is_valid_date_format(date_string):
        date_string = convert_date_format(date_string) + "Z"
    return (
        datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z").date()
        == datetime.datetime.now().date()
    )


# Converts a date string from one format to another
def convert_date_format(date_string):
    # Try to handle ordinals like 'st', 'nd', 'rd', 'th'
    for suffix in ["st", "nd", "rd", "th"]:
        if suffix in date_string:
            date_string = date_string.replace(suffix, "")
            break

    # Parse the date
    dt = datetime.datetime.strptime(date_string, "%b %d %Y")

    # Format the datetime object into the desired string format.
    # Note: the %z format code is for the UTC offset,
    # if you don't have timezone info, it'll be empty in the output.
    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")


# Checks if the date string is in the desired format
def is_valid_date_format(date_string):
    try:
        # Try to parse the date string using the desired format
        datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
        return True
    except ValueError:
        return False


# print(is_valid_date_format("2020-05-21T00:00:00Z"))
# print(convert_date_format("May 21st 2020"))
# print(is_today_from_string("May 21st 2020"))
