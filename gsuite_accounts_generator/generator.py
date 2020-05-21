import argparse
import csv
from datetime import datetime
import os
import random
import string

characters = string.ascii_letters + string.punctuation  + string.digits

def generate_accounts(num_results=1, output_csv_file=""):
    if output_csv_file == "":
        print('No output csv file provided, print out to stdout')
    else:
        # No exception handling here. In case of exception, just let it thrown.
        f = open(output_csv_file,"w")
        writer = csv.DictWriter(f, fieldnames = ["First Name [Required]", "Last Name [Required]","Email Address [Required]", "Password [Required]", "Org Unit Path [Required]"])

    random.seed(datetime.now())

    directory_path = os.path.dirname(__file__)
    adjectives, nouns = [], []
    with open(os.path.join(directory_path, 'data', 'adjectives.txt'), 'r') as file_adjective:
        for line in file_adjective:
            adjectives.append(line.strip())
    with open(os.path.join(directory_path, 'data', 'nouns.txt'), 'r') as file_noun:
        for line in file_noun:
            nouns.append(line.strip())

    org_unit_path = "/"
    accounts = {}
    for _ in range(num_results):
        firstname = random.choice(adjectives).capitalize()
        lastname = random.choice(nouns).capitalize()
    
        # GSuite account no more than 64 chars.
        email = firstname.lower()[:2] + lastname.lower()[:58] + str(random.randrange(100))
        password = "".join(random.choice(characters) for x in range(random.randint(8, 12)))

        row = {
            'First Name [Required]': firstname,
            'Last Name [Required]': lastname,
            'Email Address [Required]': email,
            'Password [Required]': password,
            'Org Unit Path [Required]': org_unit_path
        }
        
        if email in accounts.keys():
            continue

        accounts[email] = row

    if output_csv_file == "":
        for k, v in accounts.items():
            print(v)
    else:
        writer.writeheader()
        for k, v in accounts.items():
            writer.writerow(v)

def main():
    parser = argparse.ArgumentParser(description='Generate GSuite Accounts Info.')
    parser.add_argument('num_results', type=int, default=1, nargs='?',
                        help='Number of results to return')
    parser.add_argument('output_csv_file', type=str, default="", nargs='?',
                        help='Output csv file name')
    args = parser.parse_args()
    generate_accounts(num_results=args.num_results, output_csv_file=args.output_csv_file)

if __name__ == "__main__":
    
    main()