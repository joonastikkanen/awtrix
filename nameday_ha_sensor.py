import src.nameday
import datetime
import argparse

def get_nameday(nameday_csv_path):
    # Set day and month variables
    now = datetime.datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    file_path = nameday_csv_path
    nameday = src.nameday.find_nameday(file_path, day, month)
    return nameday


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Get nameday from CSV file.")
    
    # Add the arguments
    parser.add_argument("nameday_csv_path", type=str, help="Path to the nameday CSV file")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the function with the provided argument
    print(get_nameday(args.nameday_csv_path))