[![Build, Test, Deploy](https://github.com/paveldat/Gods-eye/actions/workflows/deploy-job.yml/badge.svg)](https://github.com/paveldat/Gods-eye/actions/workflows/deploy-job.yml)

# GOD'S EYE
God's EYE - Information Gathering Tool.
God's EYE is an Information Gathering Tool I made in python3.10.

## Library installation
All modules located in the `src` directory are APIs, so you can build a library from the sources and use it in your projects.

### 1. How to build a library from sources
1) Clone this repo
```shell
git clone https://github.com/paveldat/God-s-eye.git
```
2) Go to the cloned repository
```shell
cd God-s-eye
```
3) Install deb- and py-requirements
```shell
pip install -r py-requirements.txt
xargs sudo apt-get install <deb-requirements.txt
```
4) Run the following command
```shell
python3 -m build .
```
5) Now you can install library
```shell
pip install dist/gods_eye-<version>-py3-none-any.whl
```

### 2. Installation from `releases`
1) Download `.whl` file form releases
2) Run the following command:
```shell
pip install <downloaded_file>.whl
```

### 3. Installation from `PyPI`
```shell
pip install gods-eye
```

## Tools
1. Clickjacking - Checks if the clickjacking is possible on any Domain.
2. DnsLookup - Looks for dns lookup information for IP or Domain.
3. exec_shell_command - Common method to execute shell commands.
4. HttpHeadersGrabber - Looks for HTTP Headers.
5. GetHostname - Gets hostname and IP.
6. IpInfoFinder - Gets information by IP or Domain. Info: ip, status, region, country, country code, region, region name, city, zip, lat, lon,
timezone, isp, org, as.
7. Logger - Logger. The Logger has 2 handlers:
    * stream handler into console;
    * file handler into file.
8. OneSecMail - Creates one-time temporary mail.
9. PhoneInfo - Gets info by phone number.
10. PasswordPwned - Checks if password has been compromised in a data breach.
11. RobotsScanner - A robots.txt file tells search engine crawlers which URLs the crawler can access on your site. This class will search for this file, parse it and return the result.
12. WhoisLookup - Search for IP WHOIS information using the IP WHOIS lookup tool for any allocated IP address.

## How to use
Now you can use this library. To connect a module to your project, just import it.
All modules can be found in the `src` directory.

Example:
```python
from clickjacking.clickjacking import ClickJacking
```

It is not difficult to guess that the following template is used here:
`from <directory>.<filename> import <class_name>`
For example:
`from clickjacking.clickjacking import ClickJacking`

Be careful, we don't use the `src` directory anymore.

## PyPI
https://pypi.org/project/gods-eye/
