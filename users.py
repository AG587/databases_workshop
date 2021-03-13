import argparse
from models import User
from psycopg2.errors import UniqueViolation

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password (min 8 characters)")
parser.add_argument("-l", "--list")
parser.add_argument("-d", "--delete")
parser.add_argument("-e", "--edit")

args = parser.parse_args()

if args.username and args.password:
    u = User(args.username, args.password)
    try:
        u.save_user_to_db()
    except UniqueViolation:
        print("User already exists")





