# Simple SQL Injection Scanner

A simple Python script for detecting potential SQL injection vulnerabilities in a given URL and parameter.

## Purpose

The purpose of this project is to provide a basic SQL injection scanner. It checks a specified URL and parameter for potential SQL injection vulnerabilities by appending a test payload to the parameter.

## Dependencies

You will need to install the following Python packages for this project:
- `validators`

These dependencies can be installed using:

```bash
pip3 install validators
```

## Usage

To use the SQL injection scanner, run the script with the desired command-line arguments:

```bash
python sql_injection_scanner.py -u <url> -p <parameter>
```
Example:
```bash
python sql_injection_scanner.py -u https://example.com/login -p username
```

## Command Line Arguments

The script accepts the following command-line arguments:
- `-u` or `--url`: Specify the target URL.
- `-p` or `--parameter`: Provide the parameter to check for SQL injection vulnerabilities.
