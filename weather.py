import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
   
    dt = datetime.fromisoformat(iso_string)
    
    # Format the datetime into format I want
    return dt.strftime('%A %d %B %Y')

  
  
def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
# Convert temp_in_fahrenheit to a float if it's a string
    if isinstance(temp_in_fahrenheit, str):
        temp_in_fahrenheit = float(temp_in_fahrenheit)

# Convert Fahrenheit to Celsius
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5.0 / 9.0
    
    # Round to 1 decimal place
    return round(temp_in_celsius, 1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # Converting the list items into float
    weather_float_data = [float(item) for item in weather_data]
    
    # Calculate the mean
    mean_val = sum(weather_float_data) / len(weather_float_data)
    
    return mean_val

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    with open(csv_file) as weather_data_csv:
        csv_dictreader = csv.DictReader(weather_data_csv)
        return [[row["date"], float(row["min"]), float(row["max"])] for row in csv_dictreader if row]  


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    # making all the items in weather data into floats
    weather_data = [float(x) for x in weather_data]

    # Find the minimum value
    value_min = min(weather_data)
    
    # Find the index of the last minimum value
    min_index = -1

    for index in range(len(weather_data)):
        if weather_data[index] == value_min:
            min_index = index

    return (value_min, min_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    #making all in weather data into floats
    weather_data = [float(x) for x in weather_data]

    # Finding the max value
    value_max = max(weather_data)
    
    # Finding the index position of the last max value
    index_max = 0

    #using loop to find values
    for i in range(1, len(weather_data)):
        if weather_data[i] >= value_max:
            value_max = weather_data[i]
            index_max = i
    
    return (value_max, index_max)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    lowest_temp = 0
    highest_temp = 0
    sum_lowest = 0
    sum_highest = 0

    for data in weather_data:
        iso_date = data[0]  
        min_temp_f = float(data[1])
        max_temp_f = float(data[2])

        min_temp_c = convert_f_to_c(min_temp_f)
        max_temp_c = convert_f_to_c(max_temp_f)

        if(lowest_temp == 0 or lowest_temp > min_temp_c):
            lowest_temp = min_temp_c
            lowest_date = iso_date
        
        if(highest_temp < max_temp_c):
            highest_temp = max_temp_c
            highest_date = iso_date

        sum_lowest = sum_lowest + min_temp_c
        sum_highest = sum_highest + max_temp_c

    avg_lowest = sum_lowest/len(weather_data)
    avg_highest = sum_highest/len(weather_data)

    lw = round(float(lowest_temp), 1)
    hg = round(float(highest_temp), 1)
    avgl = round(float(avg_lowest), 1)
    avgh = round(float(avg_highest), 1)

    summary += (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(lw)}, and will occur on {convert_date(lowest_date)}.\n"
        f"  The highest temperature will be {format_temperature(hg)}, and will occur on {convert_date(highest_date)}.\n"
        f"  The average low this week is {format_temperature(avgl)}.\n"
        f"  The average high this week is {format_temperature(avgh)}.\n"
    )


    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for data in weather_data:
        iso_date = data[0]  
        min_temp_c = convert_f_to_c(float(data[1]))
        max_temp_c = convert_f_to_c(float(data[2]))

        summary += (
            f"---- {convert_date(iso_date)} ----\n"
            f"  Minimum Temperature: {format_temperature(min_temp_c)}\n"
            f"  Maximum Temperature: {format_temperature(max_temp_c)}\n\n"
        )

    return summary

