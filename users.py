import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-l", "--list")
parser.add_argument("-d", "--delete")
parser.add_argument("-e", "--edit")



