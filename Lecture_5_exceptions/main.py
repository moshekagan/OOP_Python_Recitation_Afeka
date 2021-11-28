class InvalidYearError(Exception):
    """Base class for other exceptions"""
    pass


def main():
    try:
        year = int(input("Please insert a birth year (0 - 2021): "))

        if year < 0 or year > 2021:
            raise InvalidYearError("Year should be between 0 to 2021!")

        age = 2021 - year
        print(f"your age is: {age}")

    except ValueError as e:
        year = 2021
        print(f"Wrong input! | {e}")
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
