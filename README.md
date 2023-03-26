# WHIP: Improving Static Vulnerability Detection in Web Application by Forcing tools to Collaborate

## Requirements
- Linux OS
- PHP (Enable Opcache)
- Python

## Installing SAST tools

Download the latest version of SAST tools
- WAP https://sourceforge.net/projects/awap/files/
- Progpilot https://github.com/designsecurity/progpilot/releases

## Tune the variables

Assign the directories in the script.php for the project, WAP, and Progpilot.

```python
# Tune these variables
project_path = "/etc/example"
project_name = "example"
Directory_to_wap = "/etc/wap-2.1"
Directory_to_progpilot = "/etc/progpilot"
```

## Run the script

Run the script 
```bash
python3 script.py
```

## Example

We provide three files as examples.

- example/a.php has code with a testability tarpit for Progpilot https://github.com/enferas/TestabilityTarpits/blob/main/PHP/TestabilityPatterns/7_string_arithmetic_operations/Pattern%20String%20Arithmetic%20Operations.md
- example/b.php has code with a testability tarpit for WAP https://github.com/enferas/TestabilityTarpits/blob/main/PHP/TestabilityPatterns/73_wrong_sanitizer/Pattern%20Wrong%20Sanitizer.md
- example/c.php has both of the tarpits.

The output of the script by using the example
```bash
Scan original project
cd /usr/src/myapp/wap; echo | timeout 900s ./wap -a -all -out /usr/src/myapp/wap/output_WAP/example.txt -p /usr/src/myapp/WHIP/example
WAP Alerts: {('/usr/src/myapp/WHIP/example/a.php', 15)}
Progpilot Alerts: {('/usr/src/myapp/WHIP/example/b.php', 17)}
Joined Alerts: {('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/b.php', 17)}
cd /usr/src/myapp/wap; echo | timeout 900s ./wap -a -all -out /usr/src/myapp/wap/output_WAP/example.txt -p /usr/src/myapp/WHIP/example
Injected Lines: {('/usr/src/myapp/WHIP/example/b.php', 13), ('/usr/src/myapp/WHIP/example/c.php', 12), ('/usr/src/myapp/WHIP/example/a.php', 11), ('/usr/src/myapp/WHIP/example/c.php', 19)}
WAP Alerts: {('/usr/src/myapp/WHIP/example/b.php', 13), ('/usr/src/myapp/WHIP/example/c.php', 13), ('/usr/src/myapp/WHIP/example/c.php', 19), ('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/c.php', 12), ('/usr/src/myapp/WHIP/example/a.php', 12), ('/usr/src/myapp/WHIP/example/a.php', 11)}
Progpilot Alerts: {('/usr/src/myapp/WHIP/example/b.php', 13), ('/usr/src/myapp/WHIP/example/c.php', 12), ('/usr/src/myapp/WHIP/example/b.php', 14), ('/usr/src/myapp/WHIP/example/a.php', 11), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Joined Alerts: {('/usr/src/myapp/WHIP/example/b.php', 13), ('/usr/src/myapp/WHIP/example/c.php', 13), ('/usr/src/myapp/WHIP/example/c.php', 19), ('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/c.php', 12), ('/usr/src/myapp/WHIP/example/a.php', 12), ('/usr/src/myapp/WHIP/example/a.php', 11), ('/usr/src/myapp/WHIP/example/b.php', 14), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Iteration 1
cd /usr/src/myapp/wap; echo | timeout 900s ./wap -a -all -out /usr/src/myapp/wap/output_WAP/example.txt -p /usr/src/myapp/WHIP/example
WAP Alerts: {('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/c.php', 19), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Progpilot Alerts: {('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/c.php', 19), ('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/b.php', 17), ('/usr/src/myapp/WHIP/example/c.php', 20)}
Joined Alerts: {('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/c.php', 19), ('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/b.php', 17), ('/usr/src/myapp/WHIP/example/c.php', 20)}
Iteration 2
cd /usr/src/myapp/wap; echo | timeout 900s ./wap -a -all -out /usr/src/myapp/wap/output_WAP/example.txt -p /usr/src/myapp/WHIP/example
WAP Alerts: {('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Progpilot Alerts: {('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Joined Alerts: {('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/b.php', 17), ('/usr/src/myapp/WHIP/example/a.php', 15)}
Scan final project
cd /usr/src/myapp/wap; echo | timeout 900s ./wap -a -all -out /usr/src/myapp/wap/output_WAP/example.txt -p /usr/src/myapp/WHIP/example
WAP Alerts: {('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Progpilot Alerts: {('/usr/src/myapp/WHIP/example/a.php', 15), ('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/b.php', 17)}
Joined Alerts: {('/usr/src/myapp/WHIP/example/c.php', 23), ('/usr/src/myapp/WHIP/example/b.php', 17), ('/usr/src/myapp/WHIP/example/a.php', 15)}
>>> New only for WAP:
('/usr/src/myapp/WHIP/example/b.php', 17)
>>> New only for Progpilot:
('/usr/src/myapp/WHIP/example/a.php', 15)
>>> New for all the tools:
('/usr/src/myapp/WHIP/example/c.php', 23)
```

The results show how our approach: 
- help WAP to detect the vulnerability in file b.php 
- help Progpilot to detect the vulnerability in file a.php
- help both of the tools to detect the vulnerability in c.php.
