import csv
import logging


FORMAT = "%(asctime)s :\t%(levelname)s\t[%(filename)s]\t%(message)s"
logging.basicConfig(filename="logging.log", format=FORMAT, level=logging.DEBUG)


def get_user_and_email(filename):
    """
    Return each row of a csv containing user and e-mail
    """
    logging.debug(f"opening {filename}")
    try:
        with open(filename, "r") as user_emails:
            reader = csv.reader(user_emails)

            # Using generator to read potentially large CSV files
            for row in reader:
                yield row
    except IOError as e:
        logging.error(f"could not open {filename}. An exception occurred!", exc_info=True)
        raise e
