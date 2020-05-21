#!/usr/bin/python
#
# https://docs.google.com/spreadsheets/d/1vePSQZIQ3y-xRKHlCxGFFKm_V10LW4UeyvXpIXrF6_w/edit#gid=0
# words/emails: words for emails
# words/passwords: words for passwords
#
# Requirements
#
# 1. Both username and password must be 8 chars long.
#
# 2. Username prefix is chosen from words/emails.  If it is less than 8 chars,
# append random numbers to make it 8 chars.
#
# 3. Password suffix is chosen from words/passwords.  If it is less than 8
# chars, prepend random numbers to make it 8 chars.
#
# 4. The first letter of the word in password is capitalized.
#
# 5. First name is always Community and last name is always Participant.
#
# 6. Generate about ~3000 users.

import csv
import random

# Filter emails and passwords which contains space and >= 8 chars.  Exclude 8
# char word to make it look consistent.
emails = [e.lower() for e in open('words/emails').read().splitlines() if ' ' not in e and len(e) < 8]
passwords = [p.lower() for p in open('words/passwords').read().splitlines() if ' ' not in p and len(p) < 8]
random.shuffle(passwords)

f = open('users.csv', 'w')
f.write('First Name [Required],Last Name [Required],Email Address [Required],Password [Required],Org Unit Path [Required]\n')

random.seed()
for email in emails:
  # [m, n)
  n = pow(10, 8-len(email))
  m = pow(10, 7-len(email))
  # For each email word, generate roughly 6 user email addresses.
  users = [email + str(i) for i in random.sample(range(m, n), 6)]
  for u in users:
    p = random.choice(passwords)
    n = pow(10, 8-len(p))
    m = pow(10, 7-len(p))
    p = str(random.choice(range(m, n))) + p.capitalize()

    f.write('{},{},{},{},{}\n'.format('Community', 'Participant', u+'@covid19communitytest.com', p, '/'))
f.close()
