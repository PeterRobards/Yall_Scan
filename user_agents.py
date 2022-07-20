#!/usr/bin/env python
"""Python tools dealing with user aganets - list of common agents + methods to select one"""
import random

# pylint: disable=line-too-long
def list_user_agents():
    """Stores lists of user agents divided by browser/os and initializes a dictionary of them """
    possible_user_agents = {}

    chrome_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    ]
    possible_user_agents["Chrome"] = chrome_user_agents

    ios_user_agents = [
        "Mozilla/5.0 (iPad; CPU OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Tablet/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/51.0.2704.104 Mobile/13F69 Safari/601.1.46",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/12B436 Safari/600.1.4 (000410)",
    ]
    possible_user_agents["iOS"] = ios_user_agents

    android_user_agents = [
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/89.0.4389.130 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Safari/537.36 EdgA/46.02.4.5147",
        "Mozilla/5.0 (Linux; Android 8.1.0; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Safari/537.36 EdgA/46.03.4.5155",
        "Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; TESLA Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; Android 8.1.0; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Safari/537.36 EdgA/46.03.4.5155",
        "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/90.0",
        "Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:90.0) Gecko/90.0 Firefox/90.0",
    ]
    possible_user_agents["Android"] = android_user_agents

    firefox_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    ]
    possible_user_agents["Firefox"] = firefox_user_agents

    safari_user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    ]
    possible_user_agents["Safari"] = safari_user_agents

    edge_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    ]
    possible_user_agents["Edge"] = edge_user_agents

    opera_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
    ]
    possible_user_agents["Opera"] = opera_user_agents

    bots_crawlers_user_agents = [
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Google (+https://developers.google.com/+/web/snippet/)",
        "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
        "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
        "ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)",
    ]
    possible_user_agents["Bots"] = bots_crawlers_user_agents

    internet_explorer_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
    ]
    possible_user_agents["IE"] = internet_explorer_user_agents

    return possible_user_agents


# pylint: enable=line-too-long


def select_from_dict(options, name):
    """Display the contents of a Dictionary and allow user to easily select one item """
    index = 0
    index_valid_list = []
    print(f"\n[+] Please select a(n) '{name}' from the list below:")
    for option_name in options:
        index = index + 1
        index_valid_list.extend([options[option_name]])
        print(f"  [{str(index)}]  '{option_name}'")

    input_valid = False

    while not input_valid:
        input_raw = input("[->] Please enter the number in front of the " + name + ": ")
        # Check if user provided a valid positive number as input
        if input_raw.isnumeric():
            # Subtract 1 from provided number to match position in list to list index
            input_num = int(input_raw) - 1
            # Check if provided number is is within the bounds of the list
            if -1 < input_num < len(index_valid_list):
                selected = index_valid_list[input_num]
                print(f"\n[+] Selected {name}:\n\t'{selected}'")
                input_valid = True
                break
        print(f"[!] Error: Please select a valid {name} number...")

    return selected


def choose_from_list(list_of_options, choice_name):
    """ Method to allow user to choose from a list of options """

    choice_dict = dict(zip(list_of_options, list_of_options))

    user_selection = select_from_dict(choice_dict, choice_name)

    return user_selection


def show_user_agents():
    """displays all available user agents"""
    user_agents = {}
    index_valid_list = []

    user_agents = list_user_agents()
    user_agent_types = list(user_agents.keys())

    print("[+] Currently Availble User Agents...")
    for agent_type in user_agent_types:
        print(f"\n[+] '{agent_type}' User Agents:")
        choices = dict(zip(user_agents[agent_type], user_agents[agent_type]))
        index = 0
        for agent in choices:
            index = index + 1
            index_valid_list.extend([choices[agent]])
            print(f"  [{str(index)}]  '{agent}'")


def list_agent_types():
    """Method to return a list of all available user agent types: types are keys in a dict"""
    all_agents = list_user_agents()
    user_agent_types = list(all_agents.keys())

    return user_agent_types


def get_random_agent(agent_type):
    """Method to randomly select a user agent from one of the available types"""
    all_agents = list_user_agents()
    random_agent = random.choice(all_agents[agent_type])
    return random_agent


def get_user_agent():
    """Returns selected type of user agent from provided dictionary, assumes types are keys"""
    user_agents = {}
    user_agents = list_user_agents()

    user_agent_types = list(user_agents.keys())

    chosen_type = choose_from_list(user_agent_types, "User Agent Type")

    type_name = str(chosen_type) + " User Agent"
    chosen_user_agent = choose_from_list(user_agents[chosen_type], type_name)

    return chosen_user_agent


def main():
    """Main driver method -- provides simple test for user agent related methods"""
    #####################################################################
    print("\n")
    print("*** " * 12)
    print("\n[*] Initializing program....\n")
    #####################################################################
    user_agent = ""
    print("[+] Compiling user agent data...")
    user_agent = get_user_agent()
    print(f"[=] Success =) User Agent is:\n\t|\n\t+-> {user_agent}")

    print("\n[*] Commencing Random choice test...")
    random_choices = {}
    print("[+] Loading user agents...")
    all_agents = list_user_agents()
    user_agent_types = list_agent_types()
    print("[+] Generating random selections...")
    for key in user_agent_types:
        random_choices[key] = random.choice(all_agents[key])

    print("[+] Random selections complete... Displaying results:")
    print("[+] User Agents:")
    for key in user_agent_types:
        agent = get_random_agent(key)
        print(f"\n[=] {key}: \n\t'{agent}'")

    print("\n[*] Displaying all current user agents...")
    show_user_agents()

    print("\n[*] Testing Complete...")
    #####################################################################
    print("[+] Exiting program!\n")
    print("*** " * 12)
    print("\n")
    #####################################################################


if __name__ == "__main__":
    main()
