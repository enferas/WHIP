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

example/a.php has code with a testability tarpit for Progpilot https://github.com/enferas/TestabilityTarpits/blob/main/PHP/TestabilityPatterns/7_string_arithmetic_operations/Pattern%20String%20Arithmetic%20Operations.md
example/b.php has code with a testability tarpit for WAP https://github.com/enferas/TestabilityTarpits/blob/main/PHP/TestabilityPatterns/28_static_methods/Pattern%20Static%20Methods.md
ecample/c.php has the two tarpits.

The output of the script by using the example
```bash
Scan original project
WAP Alerts: {('/etc/example/b.php', 4), ('/etc/example/a.php', 15)}
Progpilot Alerts: {('/etc/example/b.php', 4), ('/etc/example/b.php', 16)}
Joined Alerts: {('/etc/example/b.php', 4), ('/etc/example/b.php', 16), ('/etc/example/a.php', 15)}
Injected Lines: {('/etc/example/c.php', 26), ('/etc/example/a.php', 11), ('/etc/example/b.php', 12), ('/etc/example/c.php', 19)}
WAP Alerts: {('/etc/example/c.php', 19), ('/etc/example/b.php', 12), ('/etc/example/a.php', 11), ('/etc/example/c.php', 20), ('/etc/example/a.php', 12), ('/etc/example/a.php', 15), ('/etc/example/c.php', 26), ('/etc/example/b.php', 4)}
Progpilot Alerts: {('/etc/example/b.php', 13), ('/etc/example/c.php', 19), ('/etc/example/b.php', 12), ('/etc/example/b.php', 4), ('/etc/example/b.php', 16)}
Joined Alerts: {('/etc/example/b.php', 13), ('/etc/example/c.php', 19), ('/etc/example/b.php', 12), ('/etc/example/a.php', 11), ('/etc/example/c.php', 20), ('/etc/example/a.php', 12), ('/etc/example/a.php', 15), ('/etc/example/c.php', 26), ('/etc/example/b.php', 4), ('/etc/example/b.php', 16)}
Iteration 1
WAP Alerts: {('/etc/example/c.php', 26), ('/etc/example/a.php', 15), ('/etc/example/b.php', 4), ('/etc/example/b.php', 16)}
Progpilot Alerts: {('/etc/example/c.php', 27), ('/etc/example/c.php', 30), ('/etc/example/c.php', 26), ('/etc/example/b.php', 4), ('/etc/example/b.php', 16)}
Joined Alerts: {('/etc/example/c.php', 27), ('/etc/example/c.php', 30), ('/etc/example/a.php', 15), ('/etc/example/c.php', 26), ('/etc/example/b.php', 4), ('/etc/example/b.php', 16)}
Iteration 2
WAP Alerts: {('/etc/example/a.php', 15), ('/etc/example/b.php', 4), ('/etc/example/c.php', 30), ('/etc/example/b.php', 16)}
Progpilot Alerts: {('/etc/example/b.php', 4), ('/etc/example/c.php', 30), ('/etc/example/b.php', 16)}
Joined Alerts: {('/etc/example/a.php', 15), ('/etc/example/b.php', 4), ('/etc/example/c.php', 30), ('/etc/example/b.php', 16)}
Scan final project
WAP Alerts: {('/etc/example/a.php', 15), ('/etc/example/b.php', 4), ('/etc/example/c.php', 30), ('/etc/example/b.php', 16)}
Progpilot Alerts: {('/etc/example/b.php', 4), ('/etc/example/c.php', 30), ('/etc/example/b.php', 16)}
Joined Alerts: {('/etc/example/a.php', 15), ('/etc/example/b.php', 4), ('/etc/example/c.php', 30), ('/etc/example/b.php', 16)}
>>> New only for WAP:
('/etc/example/b.php', 16)
>>> New only for Progpilot:
('/etc/example/a.php', 15)
>>> New for all the tools:
('/etc/example/c.php', 30)
```

The results show how our approach: 
- help WAP to detect the vulnerability in file b.php 
- help Progpilot to detect the vulnerability in file a.php
- help both of the tools to detect the vulnerability in c.php.