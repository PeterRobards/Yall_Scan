#!/usr/bin/env python
"""Python tool designed to interact with URLScan.io's API and submit both URLs and UUIDs"""

import re
import os
import sys
import json
import time
import argparse
import requests

import user_agents as UA


__author__ = ["Peter Robards"]
__date__ = "7/19/2022"
__description__ = "Python tool for interacting with URLScan.io's API.\
     Submit suspicious URL's to be scanned by their site and\
     Submit UUIDs to retrieve the data associated with that scan."

########################################################################################


def get_api_key():
    """
    Method to retrieve the api key value for URLScan.io from the environment
    or, if this value is not found, prompt the user to input the key now
    """
    api_key = ""
    env_var = "URLSCAN_API_KEY"

    if env_var in os.environ:
        api_key = os.environ[env_var]
    else:
        print(
            f"\n[!] Warning: API key not detected in environment: Missing: '{env_var}'"
        )
        api_key = input("[->] Please enter your API Key for URLScan.io: ")

    return api_key


def scan_urls(urls_to_scan, headers, data):
    """Method to scan multiple URLs via URLScan.io. Returns a list of JSON responses"""

    responses = []
    scan_data = data.copy()

    for target_url in urls_to_scan:
        scan_data["url"] = target_url
        print(f"\n[*] Scanning '{target_url}' now...\n")
        response = requests.post(
            "https://urlscan.io/api/v1/scan/",
            headers=headers,
            data=json.dumps(scan_data),
        )

        responses.append(response.json())
        time.sleep(2)  # Wait 2 seconds in between url submissions.
        response = ""
        scan_data["url"] = ""

    return responses


def display_url_response(response):
    """Displays the response received from URLScan.io when submitting a URL to be scanned"""
    response_content = response.json()

    submitted_url = response_content.get("url")
    scanurl_uuid = response_content.get("uuid")
    results_link = response_content.get("result")
    status_message = response_content.get("message")
    visibility_level = response_content.get("visibility")

    print("\n[*] ScanURL.io Response Data:")
    print(f"  [+] Submitted URL:\t{submitted_url}")
    print(f"  [+] Data UUID:\t{scanurl_uuid}")
    print(f"  [+]Link to view results:\t{results_link}")
    print(f"  [+]Message:\t{status_message}")
    print(f"  [+]Scan Visibility Level:\t{visibility_level}")
    print("*** " * 12)


def error_check(content):
    """Method to check json content returned by requests library for known error codes """
    # Extract json content to check known error status
    json_content = json.loads(content.text)

    # Note: "\d+" matches one or more digits - used to find numbers in a string
    reg_ex_pattern = r"\d+"
    sleep_time = 0
    status_code = 0

    # Check for default error code '400' and/or if API quota for account has been reached
    if "status" in json_content.keys():
        status_code = json_content["status"]
        if status_code == 400:
            print(f'\n[!] Error, status returned 400:\n[-] Content:  "{content}".')
            print("[-] Exiting program...\n\n")
            sys.exit(1)
        elif status_code == 429:
            print("\n[!] Error: Status returned = '429'.")
            print("[-] Pausing scan...")
            # Note: int(re.findall(reg_ex_pattern, json_content["message"])[1]) + 5
            #  re.findall(reg_ex_pattern, json_content["message"]): extracts all numbers
            #  int(all_nmubers[1]) + 5: takes the second number in list and adds 5 to it
            sleep_time = int(re.findall(reg_ex_pattern, json_content["message"])[1]) + 5
            if sleep_time > 60:
                print(
                    f"\n[!] Warning: API submission quota exceeded, delay is {sleep_time}.\
                    \n\tVisit: 'https://urlscan.io/about-api/#ratelimit/' for more info."
                )
                print(
                    "[-] Try scan with a different privacy level selected\
                     ('Public','Private','Unlisted')."
                )
                print("[-] Quitting program...")
                sys.exit(1)
        elif status_code == 200:
            return sleep_time
        else:
            print(
                f"\n[!] Error please check input... Response status code = '{status_code}'"
            )
            print(f"[-] Description: {content}.")
            print("[-] Quitting program...")
            sys.exit(1)
    return sleep_time


def replay_request(response, headers, data, delay, target_url):
    """Resubmit request URLScan.io, repeats up to 5 attempts, exits on failure"""

    counter = 0
    while delay != 0:
        attempts = counter + 1

        # A delay of 0 means no errors detected
        # otherwise delay should be between 1 and 60
        if 0 < delay <= 60:
            print(f"[-] Repeating scan in {delay} seconds...")
            print(f"[-] There have been: '{attempts}' scans attempted.")
            if ask_question("Would you like to QUIT now instead?"):
                print("[-] Quitting program...")
                sys.exit(1)
            time.sleep(int(delay))
            response = requests.post(
                "https://urlscan.io/api/v1/scan/",
                headers=headers,
                data=json.dumps(data),
            )

        elif delay == 0:
            break
        else:
            print(
                f"\n[!] Error: value for time delay: '{delay}' is out of expected bounds..."
            )
            print("[-] Quitting program...")
            sys.exit(1)

        if attempts >= 5:
            print(f"[!] Error: There have been '{attempts}' failed scan attempts!")
            print(f"[-] Please check target url: /'{target_url}/'")
            print("[-] Quitting program...")
            sys.exit(1)
        # Increment counter for each iteration of this loop
        # quit after 5 attempts (counter will = 4)
        counter += 1
        delay = error_check(response)

    return response


########################################################################################


def ask_question(question="Would you like to continue?"):
    """Provide a Yes or No question and prompt user for the answer. Returns True/False"""
    answer = False

    while not answer:

        print(f"\n[?] {question}", end=" ")
        answer = input("\t[Yes or No]: ")

        if answer[0].lower() == "y":
            answer = True
            break
        if answer[0].lower() == "n":
            answer = False
            break

        print(f"\n[!] ERROR - your response: '{answer}' is invalid!")
        print('[-] Please type either "Yes" or "No"!\n')

    return answer


########################################################################################


def extract_urls(json_responses):
    """Method to extract the UUID value from a JSON formatted"""
    urls = []
    if isinstance(json_responses, list):
        for json_object in json_responses:
            json_data = json_object
            this_url = json_data.get("url")
            urls.append(this_url)
    else:
        this_url = json_responses.get("url")
        urls.append(this_url)

    return urls


def extract_uuids(json_responses):
    """Method to extract the UUID value from a JSON object"""
    uuids = []
    if isinstance(json_responses, list):
        for json_object in json_responses:
            json_data = json_object
            this_uuid = json_data.get("uuid")
            uuids.append(this_uuid)
    else:
        this_uuid = json_responses.get("uuid")
        uuids.append(this_uuid)

    return uuids


def get_uuids_data(uuids_to_scan, options):
    """
    Method to retrieve the data associated with multiple UUIDs via URLScan.io.
    Returns a list of JSON formatted objects
    """
    content = []
    for uuid in uuids_to_scan:
        scan_content = get_uuid_data(uuid)
        content.append(scan_content)

        # Download site PNG and/or DOM from provided uuid
        if options.get_png:
            get_uuid_png(uuid, options.out_dir)
        if options.get_dom:
            get_uuid_dom(uuid, options.out_dir)

    return content


########################################################################################
# pylint: disable=E1101
# Note: E1101: Instance of 'LookupDict' has no 'ok' member (no-member)


def get_uuid_data(uuid):
    """Method to retrieve the scan results from URLScan.io with a provided UUID"""
    target_url = "https://urlscan.io/api/v1/result/" + uuid

    print(f"[+] Submitting request to target url: '{target_url}'...")
    response = requests.get(target_url)

    status = response.status_code

    if status != requests.codes.ok:
        print(
            f"[!] Error Data retrieval for uuid: '{uuid}' \
        failed with status: '{status}'."
        )
        print("[-] Exiting program...")
        sys.exit(5)

    print("[+] Successfully retrieved UUID data!")

    return response.json()


def get_uuid_dom(uuid, out_dir):
    """Retrieve the site DOM from URLScan.io associated with a provided UUID"""
    target_url = "https://urlscan.io/dom/" + uuid
    response = requests.get(target_url)
    status = response.status_code

    if status != requests.codes.ok:
        print(f"[!] Error: DOM retrieval failed with status: '{status}'.")
    else:
        out_file = out_dir + "/DOM_" + str(uuid) + ".html"
        content = response.content
        with open(out_file, "wb") as o_f:
            o_f.write(content)


def get_uuid_png(uuid, out_dir):
    """Retrieve the site PNG result from URLScan.io associated with a provided UUID"""
    target_url = "https://urlscan.io/screenshots/" + uuid + ".png"
    response = requests.get(target_url)
    status = response.status_code

    if status != requests.codes.ok:
        print(f"[!] Error: PNG retrieval failed with status: '{status}'.")
    else:
        out_file = out_dir + "/" + str(uuid) + ".png"
        content = response.content
        with open(out_file, "wb") as o_f:
            o_f.write(content)


# pylint: enable=E1101
########################################################################################


def validate_file(file_path):
    """ Method to check if a provided file path exists and exit with error message if not"""
    if os.path.isfile(file_path):
        return

    print("[!] Error: File not found!")
    print(f"[-] Please check input: '{file_path}'")
    print("[-] Exiting program...")
    sys.exit(2)


def read_in_json(file_name):
    """ Read in JSON data from a file"""
    json_data = {}
    with open(file_name, "r", encoding="utf8") as in_file:
        json_data = json.load(in_file)

    return json_data


def read_in_nline(file_name):
    """ Read in data from a file, splitting it up line by line"""
    with open(file_name, "r", encoding="utf8") as in_file:
        data = in_file.read().splitlines()
    return data


def create_directory(directory_path):
    """Method to create a new directory if it does not already exist"""
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"[=] Directory: '{directory_path}' created successfully!")
    except OSError as error:
        print(
            f"[!] Error: Directory: '{directory_path}' can not be created...\n\\'{error}'"
        )


def save_json_content(out_file, json_content):
    """ Method to save a JSON formatted content to a provided file path """
    with open(out_file, "w", encoding="utf8") as o_f:
        json.dump(json_content, o_f, ensure_ascii=False, indent=4)


def save_list_to__file(out_file, content):
    """Method to save content stored in a list to a file with each entry on a new line"""
    with open(out_file, mode="w", encoding="utf-8") as o_f:
        o_f.write("\n".join(content))


########################################################################################

########################################################################################


def main():
    """Main driver method -- program provides interface to interact with URLScan.io API"""
    #####################################################################
    # Initialize Program Menu
    parser = argparse.ArgumentParser(
        description=__description__,
        epilog=f"Last Modified by {__author__} on {__date__}",
    )
    parser.add_argument(
        "--url",
        dest="input_url",
        help="Input a single URL to scan.",
    )
    parser.add_argument(
        "--uuid",
        dest="input_uuid",
        help="Input a single UUID to retrieve information on.",
    )
    parser.add_argument(
        "--url_file",
        dest="url_file",
        help="Enter the path to a File containing a list of URL's to scan.",
    )
    parser.add_argument(
        "--uuid_file",
        dest="uuid_file",
        help="Enter the path to a File containing a list of UUID's to retrieve data for.",
    )
    parser.add_argument(
        "--response_file",
        dest="response_file",
        help="Enter the path to a File containing response generated by submitting a URL.",
    )
    parser.add_argument(
        "-o",
        "--output_location",
        dest="out_dir",
        help="name of the Directory where you want to save results.",
    )
    parser.add_argument(
        "--scan_type",
        dest="scan_type",
        help="Type of scan you wish to perform.",
        choices=("public", "unlisted", "private"),
        default="unlisted",
    )
    parser.add_argument(
        "-U",
        "--user_agent",
        dest="user_agent",
        help="Signal you wish to select a specific user agent instead of default iOS.",
        action="store_true",
    )
    parser.add_argument(
        "-T",
        "--tags",
        dest="tags",
        nargs="+",
        help="Used with URLs: Submit list (1-10 items) of tags to be associated with URL(s).",
    )
    parser.add_argument(
        "-X",
        "--export_uuids",
        dest="export_uuids",
        help="Used with URL(s): Signals to export UUID(s) to file formatted for this tool.",
        action="store_true",
    )
    parser.add_argument(
        "--png",
        dest="get_png",
        help="Signal you wish to download the PNG associated with provided UUID.",
        action="store_true",
    )
    parser.add_argument(
        "--dom",
        dest="get_dom",
        help="Signal you wish to download the DOM associated with provided UUID.",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--country_code",
        dest="country_code",
        help="Country code that you wish the scan to originate from.",
        choices=("de", "us", "jp", "fr", "gb", "nl", "ca", "it", "es"),
        default="us",
    )

    # Check for above arguments - if none are provided, Display --help and exit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Load menu options
    options = parser.parse_args()
    #####################################################################

    #####################################################################
    # Initialize variables
    time_delay = 0
    target_url = ""
    target_uuid = ""

    json_file_data = {}
    responses = []
    urls_to_scan = []
    uuids_to_save = []
    uuids_to_scan = []
    uuid_responses = []

    print("\n")
    print("*** " * 12)
    print("\n[*] Initializing program....\n")

    # Process target URL(s) and/or UUID(s) to scan
    if options.input_url:
        target_url = options.input_url
    elif options.input_uuid:
        target_uuid = options.input_uuid
    elif options.url_file:
        # Check to make sure the provided file exists, if not show error message and exit
        validate_file(options.url_file)
        # Read in URL's from a file where each URL is on a separate line
        urls_to_scan = read_in_nline(options.url_file)
    elif options.uuid_file:
        # Check to make sure the provided file exists, if not show error message and exit
        validate_file(options.uuid_file)
        # Read in UUID's from a file where each UUID is on a separate line
        uuids_to_scan = read_in_nline(options.uuid_file)
    elif options.response_file:
        # Check to make sure the provided file exists, if not show error message and exit
        validate_file(options.response_file)
        json_file_data = read_in_json(options.response_file)
        if ask_question("Select UUID from file to submit?"):
            uuids_to_scan = extract_uuids(json_file_data)
        elif ask_question("Select URL from file to submit?"):
            urls_to_scan = extract_urls(json_file_data)
    else:
        target_url = input(
            "[->] Please enter the suspicious URL you would like to scan: "
        )
    #####################################################################

    #####################################################################
    # Check environment for URLSCAN API Key
    #  if not found prompt user for their api key
    api_key = get_api_key()

    # Initialize user agent variable for http POST request to URLScan.io
    if options.user_agent:
        # Asks user to select a type of user agent (e.g. iOS, Android, Chroms, etc)
        #  and then asks the user to select a specific user agent of that type.
        user_agent = UA.get_user_agent()

    else:
        # Randomly select a user agent of the "iOS" type
        user_agent = UA.get_random_agent("iOS")
    #####################################################################

    #####################################################################
    # Set header and data options for request to URLScan.io
    #  privacy_level = ["Public", "Unlisted", "Private"]
    #  source_country = Country code that you wish the scan to originate from (default = 'us')
    privacy_level = options.scan_type
    source_country = options.country_code

    # Check if tags have been provided and take the first 10 (if more than 10 provided)
    # Note: URLScan.io limits the number of tags to 10
    tags = []
    if options.tags:
        if len(options.tags) > 10:
            print(
                f"\n[!] Warning: MAX number of tags is 10 - you provided: '{len(options.tags)}'"
            )
            print("[-] Submitting only the first 10 tags:")
            tags = options.tags[0:10]
            print(f"\t{tags}")
        else:
            tags = options.tags

    headers = {"API-Key": api_key, "Content-Type": "application/json"}
    data = {
        "url": "",
        "visibility": privacy_level,
        "customagent": user_agent,
        "country": source_country,
        "tags": tags,
    }

    #####################################################################
    # Create Directory to save results...
    if options.out_dir:
        save_dir = options.out_dir
    else:
        save_dir = input(
            "\n[->] Please enter the Directory name where you wish to save the results: "
        )

    create_directory(save_dir)

    #####################################################################

    #####################################################################
    # Submit http POST request to URLScan.io and retrieve response(s)
    if urls_to_scan:
        responses = scan_urls(urls_to_scan, headers, data)
        if options.export_uuids:
            uuids_to_save = extract_uuids(responses)

    elif target_url:
        data["url"] = target_url
        print(f"\n[+] Scanning '{target_url}' now...")
        response = requests.post(
            "https://urlscan.io/api/v1/scan/", headers=headers, data=json.dumps(data)
        )

        print("[-] Checking Response...")

        time_delay = error_check(response)
        if time_delay != 0:
            response = replay_request(response, headers, data, time_delay, target_url)

        if response:
            if ask_question("[?] Would you like to view the URL submission results?"):
                display_url_response(response)

    #####################################################################

    #####################################################################
    # Submit http POST request to URLScan.io and retrieve data associated with provided UUID
    if uuids_to_scan:
        uuid_responses = get_uuids_data(uuids_to_scan, options)
    elif target_uuid:
        print(f"\n[*] Retrieving scan results associated with UUID: '{target_uuid}'...")
        scan_content = get_uuid_data(target_uuid)

        # Download site PNG and/or DOM from provided uuid
        if options.get_png:
            get_uuid_png(target_uuid, save_dir)
        if options.get_dom:
            get_uuid_dom(target_uuid, save_dir)

    #####################################################################

    #####################################################################
    # Save results
    if responses:
        save_file = save_dir + "/URLScan_Results_urls.json"
        save_json_content(save_file, responses)
        print(f"[*] Results saved to: '{save_file}'...")

    if options.export_uuids:
        save_file = save_dir + "/UUIDs.json"
        save_list_to__file(save_file, uuids_to_save)
        print(f"[*] List of UUIDs saved to: '{save_file}'...")

    if target_url:
        save_file = (
            save_dir
            + "/"
            + "URLScan_"
            + target_url.replace("/", "_")
            + "_Response.json"
        )
        save_json_content(save_file, response.json())
        print(f"[*] Results saved to: '{save_file}'...")

    if uuid_responses:
        save_file = save_dir + "/URLScan_Results_uuids.json"
        save_json_content(save_file, uuid_responses)
        print(f"[*] Results saved to: '{save_file}'...")

    if target_uuid:
        save_file = save_dir + "/URLScan_" + target_uuid + ".json"
        save_json_content(save_file, scan_content)
        print(f"[*] Results saved to: '{save_file}'...")

    #####################################################################

    #####################################################################

    #####################################################################
    print("[+] Operations complete!\n")
    print("*** " * 12)
    print("\n")
    #####################################################################


if __name__ == "__main__":
    main()
