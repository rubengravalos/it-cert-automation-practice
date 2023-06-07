#!/usr/bin/env python3

import psutil
import socket
import emails

sender = "automation@example.com"
recipient = "student-00-e6bd6c6f448c@example.com"
body = "Please check your system and resolve the issue as soon as possible"

""" cpu_usage > 80 """
cpu_usage = psutil.cpu_percent(interval=1)

""" percent parameter represents the utilization. percent > 80 """
disk_usage = psutil.disk_usage('/')

""" mem.available < 5e8 """
mem = psutil.virtual_memory()

if cpu_usage > 80.0 :
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.generate_error_report(message)

if disk_usage.percent > 80.0 :
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.generate_error_report(message)

if mem.available < 5e8 :
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.generate_error_report(message)

if socket.gethostbyname("localhost") != "127.0.0.1" :
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.generate_error_report(message)