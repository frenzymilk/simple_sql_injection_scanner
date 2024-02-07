
import argparse
import requests

#installed packages
import validators

"""
    command line arguments
"""
parser = argparse.ArgumentParser(
    prog='Simple SQL injection scanner'
    )
# url
parser.add_argument(
    "-u",
    "--url",
    required=True,
    help="Provide the url to evaluate"
    )
# parameter
parser.add_argument(
    "-p",
    "--parameter",
    required=True,
    help="Provide the parameter to check")

args = parser.parse_args()

url = args.url
parameter = args.parameter

def sql_injection_scanning(url, parameter):
    complete_url = url + "?" + parameter + "=test' OR '1'='1"
    print(f"Final url: {complete_url}")
    r = requests.get(complete_url)

    if "error" in r.text or "exception" in r.text:
        print("Sql injection detected fofr {url}")

if not validators.url(url):
    print("Please provide a valid url")
    exit()

sql_injection_scanning(url, parameter)