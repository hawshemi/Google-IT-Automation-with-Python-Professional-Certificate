#!/usr/bin/env python3


import os
import datetime
import reports
import emails


dt = datetime.date.today().strftime("%B  %d, %Y")
date = "Processed Update on " + dt
names = []
weights = []
path = "./supplier-data/descriptions/"
for file in os.listdir("./supplier-data/descriptions"):
    with open(path + file) as f:
        for ln in f:
            line = ln.strip()
            if len(line) <= 10 and len(line) > 0 and "lb"not in line:
                fruit_name = "name: " + line
                names.append(fruit_name)
            if "lbs" in line:
                fruit_weight = "weight: " + line
                weights.append(fruit_weight)

summary = ""
for name, weight in zip(names, weights):
    summary += name + '<br />' + weight + '<br />' + '<br />'

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)