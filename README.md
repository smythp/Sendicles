

## Sendicles

A lightweight bulk mailer for Python

### Dependencies

Python 2.7
jinja2 (pip install jinja2)

### Getting Started

1. Clone the repository.
2. Install jinja2 (pip install jinja2)
3. Add Gmail credentials to sendmail.py
4. Add recipients and template fields to list.csv
5. Edit /emails/tempaltes/email1.html with your email tempalte
6. If fields have been added to .csv, add them to the list following `email_out = template.render` in sendmail.py
7. Run the script with `python sendmail.py` or `chmod a+x sendmail.py;./sendmail.py`
