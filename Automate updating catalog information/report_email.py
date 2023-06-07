#!/usr/bin/env python3

import os
import datetime
import reports
import emails

if __name__ == "__main__":
    text_files = os.listdir(os.getcwd()+"/supplier-data/descriptions/")
    paragraph = ""
    title = "Processed Update on " + datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    attachment = "processed.pdf"

    for file in text_files:
        with open('supplier-data/descriptions/'+file, 'rb') as opened:
            paragraph += opened.readline().decode("utf-8")+"<br/>"+opened.readline().decode("utf-8")+"<br/>"+"<br/>"
    
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    recipient = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)
    