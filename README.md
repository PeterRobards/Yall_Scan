# Yall Scan
Python tool for interacting with [URLScan.io's API](https://urlscan.io/docs/api/). 
Submit suspicious [URLs](#URLs) to be scanned by their website and submit [UUIDs](#UUIDs) to retrieve the associated data.

## Getting Started

This tool is designed to work with the website [URLScan.io](https://urlscan.io) and in order to properly function it requires an API Key.

### Prerequisites

This tool is optimized for [Python](#Python) 3.9x and above.

This tool requires an API Key from [URLScan.io](https://urlscan.io) in order to work.

To get an API Key to use with this tool, visit the website linked above and sign up for an account.
They currently (as of July 2022) offer a Free account that allows for up to 
5,000 public url submissions per day (60/minute) and 10,000 result requests per day 
Note: these quotas reset at Midnight UTC.

Once you obtain an [API Key](#API-KEY) from URLSCan you can either save it to use as an 
environmental variable or enter it into the program directly when [prompted](#API-KEY). 


## Python

Python 3 is essential for running this program and, while not required, I always suggest setting up a
python virtual environment (venv) or (pipenv) when running this tool in order to keep your workspace isolated.

If you already know you have an appropriate version of Python installed on your system, you can skip to either:
Setting up a [Virtual Environment](#VirtualEnvironment), installing the [Requirements](#Requirements), or directly to [Usage](#Usage) 
if all the other [Prerequisites](#Prerequisites) have been met.

If you know you're missing Python3, you can find and download the appropriate package for your OS via the link below.
If you're unsure, or you have never installed Python before check out the next section about installing python.

* [Python.org](https://www.python.org/getit/) - Get Python here!

## Installing Python

First check to see if Python is installed on your system and if so, what version is running. 
How that process works depends largely on your Operating System (OS).
If Python is not already on your system, or it is not version 3.9x or above, then you'll need to install it or update it.

Detailed instructions for installing Python3 on Linux, MacOS, and Windows, are available at link below:

* [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) - How to install Python!

## Package Management with pip

Once you have verified that you have Python 3.x installed and running on your system, you'll be using the built in
package manager 'pip' to handle the rest of the installations. 

pip is the reference Python package manager and is used to install and update packages. 
You’ll need to make sure you have the latest version of pip installed on your system.

### Linux

Note: Debian and most other distributions include a python-pip package. If, for some reason, you prefer to use 
one of the Linux distribution-provided versions of pip instead vist [https://packaging.python.org/guides/installing-using-linux-tools/].
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python -m pip --version

# Check the Python 3 version
$ python3 -m pip --version
```
You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
# Upgrade pip
$ python -m pip install --user --upgrade pip

# Upgrade pip python3
$ python3 -m pip install --user --upgrade pip
```

### Windows

The Python installers for Windows include pip. You should be able to see the version of pip by opening ‘cmd’ (the Command Prompt) and entering the following: 

```
C:\> python -m pip --version

```
You can make sure that pip is up-to-date by running:
```
C:\> python -m pip install --upgrade pip

```

### Mac OSX

 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python -m pip --version

# Check the Python 3 version
$ python3 -m pip --version
```
You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
# Upgrade pip
$ python -m pip install --user --upgrade pip

# Upgrade pip python3
$ python3 -m pip install --user --upgrade pip
```

## VirtualEnvironment

It is recommended that you create a virtual environment in order to perform operations with this program on your system, 
this will need to be accomplished before installing any further dependencies this tool relies on.
The 'venv' module is the preferred way to create and manage virtual environments for this tool. 
Luckily since Python 3.3m venv is included in the Python standard library.
 Below are the steps needed to create a virtual environment and activate it in the working directory for this tool.

### Linux

To create a virtual environment, go to your project’s directory and run venv, as shown below:
```
# If you only have Python3 installed or Python3 is set as your default
$ python -m venv env

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 -m venv env
```

### Windows

To create a virtual environment, go to your project’s directory and run venv, as shown below: 

```
C:\> python -m venv env

```

### Mac OSX

To create a virtual environment, go to your project’s directory and run venv, as shown below: Double check your system's version by using the following commands:
```
# If you only have Python3 installed or Python3 is set as your default
$ python -m venv env

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 -m venv env
```

Note: The second argument is the location to create the virtual environment.
so according to the above commands: venv will create a virtual Python installation in the env folder.
In general, you can simply create this in your project yourself and call it env (or whatever you want).

Tip: You should be sure to exclude your virtual environment directory from your version control system using .gitignore or similar.

## Activating the Virtual Environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment
serves to put the virtual environment-specific python and pip executables into your shell’s PATH.

### Linux

To create a virtual environment, go to your project’s directory and run venv, as shown below:
```
$ source env/bin/activate
```

### Windows

To create a virtual environment, go to your project’s directory and run venv, as shown below: 

```
C:\> .\env\Scripts\activate

```

### Mac OSX

To create a virtual environment, go to your project’s directory and run venv, as shown below: Double check your system's version by using the following commands:
```
$ source env/bin/activate
```
Now the development environment has been properly set up with an up to date version of Python 3 you're ready to install the required dependencies.


## Requirements

The main external library that this tool requires is the `requests` module, which has its own prerequisites included below.
Included in this repository should be a 'requirements.txt' file, with the required libraries formatted as shown below.

```
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
requests==2.27.1
urllib3==1.26.9

```

To install these dependencies via the 'requirements.txt' file, simply use  `pip -m install -r requirements.txt`

### Linux

Make sure the document 'requirements.txt' is in your current working directory and run:
```
$ python -m pip install -r requirements.txt
```

### Windows

Make sure the document 'requirements.txt' is in your current working directory and run: 

```
C:\> python -m pip install -r requirements.txt

```

### Mac OSX

Make sure the document 'requirements.txt' is in your current working directory and run:
```
$ python -m pip install -r requirements.txt
```

Once you have installed the few required dependencies and obtained your API Key for URLScan, then you're ready to go.


## API-KEY

When using this tool to submit a URL or retrieve the results related to a UUID the program will first check for an API Key saved in the
Environment as a variable named: "URLSCAN\_API\_KEY".

````
# To set variable only for the current shell:
$ URLSCAN_API_KEY="YOUR-API-KEY"

# To set it for the current shell and all processes spawned from the current shell:
$ export URLSCAN_API_KEY="YOUR-API-KEY"
````

If the "URLSCAN\_API\_KEY" is not found in the environment, the program will prompt the user to enter their key with the following message:
````
[!] Warning: API key not detected in environment: Missing: 'URLSCAN_API_KEY'
[->] Please enter your API Key for URLScan.io: 

````


## Usage

Once you're ready to run this program for the first time, running either `python yall_scan.py` or `python yall_scan.py -h`
will bring up the information you see included below. This details the various optional arguments the program takes.

In order to work properly this tool requires either a single url (--url) / uuid (--uuid) or the file path to
a file containing multiple urls (--url\_file), uuids (--uuid\_file), or responses (--response\_file).


````
$ python yall_scan.py

usage: yall_scan.py [-h] [--url INPUT_URL] [--uuid INPUT_UUID] [--url_file URL_FILE]
                    [--uuid_file UUID_FILE] [--response_file RESPONSE_FILE] [-o OUT_DIR]
                    [--scan_type {public,unlisted,private}] [-U] [-T TAGS [TAGS ...]]
                    [-X] [--png] [--dom] [-c {de,us,jp,fr,gb,nl,ca,it,es}]

Python tool for interacting with URLScan.io's API. Submit suspicious URL's to be scanned
by their site and Submit UUIDs to retrieve the data associated with that scan.

optional arguments:
  -h, --help            show this help message and exit
  --url INPUT_URL       Input a single URL to scan.
  --uuid INPUT_UUID     Input a single UUID to retrieve information on.
  --url_file URL_FILE   Enter the path to a File containing a list of URL's to scan.
  --uuid_file UUID_FILE
                        Enter the path to a File containing a list of UUID's to retrieve
                        data for.
  --response_file RESPONSE_FILE
                        Enter the path to a File containing response generated by
                        submitting a URL.
  -o OUT_DIR, --output_location OUT_DIR
                        name of the Directory where you want to save results.
  --scan_type {public,unlisted,private}
                        Type of scan you wish to perform.
  -U, --user_agent      Signal you wish to select a specific user agent instead of
                        default iOS.
  -T TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        Used with URLs: Submit list (1-10 items) of tags to be
                        associated with URL(s).
  -X, --export_uuids    Used with URL(s): Signals to export UUID(s) to file formatted
                        for this tool.
  --png                 Signal you wish to download the PNG associated with provided
                        UUID.
  --dom                 Signal you wish to download the DOM associated with provided
                        UUID.
  -c {de,us,jp,fr,gb,nl,ca,it,es}, --country_code {de,us,jp,fr,gb,nl,ca,it,es}
                        Country code that you wish the scan to originate from.
````

The typical workflow for this tool would be: Submit a suspicious URL and retrieve a response that contains
a UUID and URL linking to the results of the scan which is viewable on URLSCan's website. This response is saved.
Then you can either choose to submit the UUID returned in the response to download the raw data in JSON format for
use in other tools or you can visit the results link in order to examine the results via URLScan's great web GUI.
You can also use the UUID to download a screenshot of the site (--png) and the Document Object Model (--dom) when available.

This tool also accepts multiple URLs/UUIDs as input via a file path. It is important to note that for both URL files (--url\_file)
and UUID files (--uuid\_file) that the expected format is: a single item (be it URL or UUID) per line as the program will read in 
a file line by line, saving the text of each line into a list for late submission.

When submitting multiple URL's using the optional argument: `-X` or `--export_uuids` will automatically extract the UUID's associated
with each submitted URL from the response and save them in a UUID file that is properly formatted to work with this tool.
Also the (--response\_file) argument is designed to work with responses saved by this tool from submitting URLs. This option
allows you to specify a previously saved response file and select either the URLs or UUIDs saved in the file and auto submit them.


### URLs

If you have a single suspicious URL that you want to submit to URLSCan.io so you can investigate it further,
Then you'll want to use the `--url` argument. Below is an example of how that might look.
Note: if an output location (i.e. the directory where you want to save the results: `-o`) is not specified ahead of time, the program
will prompt you to specify one before saving the results.

````
$ python yall_scan.py --url suspicious.url -o SomeDirectory -T tag1 tag2 tag3
````

The optional arguments that you can use with any type or URL submission include:
````
  --scan_type {public,unlisted,private}
                        Type of scan you wish to perform: Sets visibility level of scan.
                        Note: defaults to whatever you have set on your URLScan.io account.
                        
  -U, --user_agent      Signal you wish to select a specific user agent from a provided list 
                        instead of the default: a random iOS user agent.
  
  -T TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        User defined Tags: Submit a list (1-10 items) of tags to be
                        associated with URL(s) on URLScan.io's website. If more than 10
                        tags are included, the program will only sumit the first 10 tags.
  -c {de, us, jp, fr, gb, nl, ca, it, es}, --country_code {de,us,jp,fr,gb,nl,ca,it,es}
                        Country code that you wish the scan to originate from.
                        Works with "public" visibility scan_type.
````

Submitting multiple URLs that have been saved to a file called "File\_Name.txt" would look like this:

````
$ python yall_scan.py --url_file file_name.txt -o SomeDirectory -T tag1 tag2 tag3 -X
````
Note: if you are submitting multiple URLs at once (via `--url_file`) you can use use the option: `-X` or `--export_uuids`
to automatically extract the UUIDs from the responses returned by URLScan into a file formatted for use with this program.

### UUIDs

If you have already submitted a suspicious URL to URLScan.io and you want to retrieve the raw JSON data associated with the scan
then you will want to use the `--uuid` argument. You can retrieve the UUID for a scan either from the website or view it in the response
returned by the URL submission function of this program. Upon submitting a UUID via this tool, the JSON data will be saved in a file inside
the user designated output directory.

See below for an example of how to submit a single UUID:
````
$  python yall_scan.py --uuid Urlscan-UUID-Goes-Here -o SomeDirectory --png --dom
````
Note: the options: `--png` downloads a screenshot of the site, and `--dom` downloads the Document Object Model when available.
These options are available for both single UUIDs and bulk UUID submissions.

Submitting multiple UUIDs that have been saved to a file called "File\_Name.txt" would look like this:
````
$ python yall_scan.py --uuid_file file_name.txt -o SomeDirectory
````

### Responses

Finally, this program can also accept a response file - as generated by a URL submission - this file will be in JSON format
and contain information regarding the URL that was scanned, a UUID associated with the scan, various links to view the results,
and a host of other information (e.g. scan visibility, country code, user agent, etc.). 

Below is an example of what a typical json response returned by URLScan.io looks like:
````
{
    "message": "Submission successful",
    "uuid": "Urlscan-UUID-Goes-Here-0xd34db33f",
    "result": "https://urlscan.io/result/Urlscan-UUID-Goes-Here-0xd34db33fe/",
    "api": "https://urlscan.io/api/v1/result/Urlscan-UUID-Goes-Here-0xd34db33f/",
    "visibility": "public,
    "options": {
        "useragent": "Mozilla/5.0 (Device_info) (KHTML, like Gecko) User_Agent/101.9"
    },
    "url": "http://scanned.url/site.php",
    "country": "us"
}

````

This tool will allow you to select either the UUID or the URL to be extracted from this data and then automatically either
submit that URL to be scanned again (this is handy if you want to scan the same URL with different options, e.g. Country code or User Agent)
or retrieve the raw JSON data associated with the UUID(s). This method works with both a file containing a single response or multiple responses. 

Processing a response file that is names "Response\_File.json" would look like this:

````
$ python yall_scan.py --response_file Reponse_File.json -o SomeDirectory
````

The program will then ask if you want to extract either the UUID or URL and then proceed accordingly.
Note: if you plan to extract the URL from the file you can use the optional arguments associated with URLs
(`--scan_type`, `--user_agent`, `--tags`, `--country_code`) at the command line in order to use them in the resulting scan(s).
