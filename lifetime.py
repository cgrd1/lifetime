from datetime import date
import sys
import inflect


def main():

    p = inflect.engine()
    
    birth_date = input("Date of birth: ")

    days = convert(birth_date)

    days, remove = str(days).split(" days")

    days_remaining = 28835 - int(days)

    days_remaining = p.number_to_words(str(days_remaining))

    print(f"{days_remaining} days remaining ... for your 79th birthday! 🥳".capitalize())


# Counts days since date of birth as a timedelta object
def convert(birth_date):
    
    try:
    
        year, month, day = birth_date.split("/")

        d = date(int(year), int(month), int(day))
        
        return date.today() - d

    except ValueError:

        sys.exit("Please enter your date of birth as YYYY/MM/DD")


if __name__ == "__main__":
    main()