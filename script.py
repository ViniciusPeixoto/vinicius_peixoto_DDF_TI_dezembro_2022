# This script must be executed in admin mode otherwise the command will not run
# If you get an "Access Denied" message, run with administrator privileges

import platform
import logging
import subprocess as sub
from lib.utils import get_user_and_email

FORMAT = "%(asctime)s :\t%(levelname)s\t[%(filename)s]\t%(message)s"
logging.basicConfig(filename="logging.log", format=FORMAT, level=logging.DEBUG)


def main():
    # check to see if the script is running on Windows
    if platform.system() != "Windows":
        logging.warning("This script is meant to run in Windows systems. Aborting...")
        print("This script is meant to run in Windows systems. Aborting...")
        return

    # iterating through every line in "users_emails.csv" file
    logging.debug("calling generator to get data")
    for user, user_email in get_user_and_email("users_emails.csv"):
        try:
            # creating a new Windows user passing the email as the user's full name
            exec = sub.Popen(["net", "user", user, "/ADD", f"/fullname:\"{user_email}\""], shell=True)
            logging.info(f"output for user \"{user}\": {exec.returncode}")
            exec.wait()
        except Exception as e:
            logging.error(f"could not process user {user}. An exception occurred!", exc_info=True)
            raise e


# "main" is only called when this file is executed and not when imported
if __name__ == "__main__":
    logging.debug("script is being initiated")
    main()
    logging.debug("script is being terminated as expected")
