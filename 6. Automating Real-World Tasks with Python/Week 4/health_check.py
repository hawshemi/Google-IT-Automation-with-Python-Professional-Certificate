#!/usr/bin/env python3


import shutil
import psutil
import socket
import emails
import os


sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

# Checks disk usage and sends email if available space < 20%
du = shutil.disk_usage("/")
du_prsnt = du.free/du.total * 100
if du_prsnt < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Checks CPU usage and sends email if usage >80%
cpu_prsnt = psutil.cpu_percent(1)
if cpu_prsnt > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Checks for available memory, if < 500mb sends an email
mem = psutil.virtual_memory()
trs = 500 * 1024 * 1024  # 500MB
if mem.available < trs:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Checks hostname and if cannot be resolved to "127.0.0.1" sends an email
hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)