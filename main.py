#!/usr/bin/env python
from MySQLdb import _mysql
import argparse
import pyfiglet


# * parse the command line arguments
parser = argparse.ArgumentParser(description='A simple Password Manager')
parser.add_argument('-s', '--site', type=str, metavar='',
                    help='The website you want to retrieve credentials for')
parser.add_argument('-b', '--banner', action='store_true',
                    help='display banner')
parser.add_argument('-m', '--mode', type=str, metavar='',
                    help='Speficy operation mode, add for entry or get for retrieval')
parser.add_argument('-u', '--username', type=str, metavar='',
                    help='your username or email')
parser.add_argument('-p', '--password', type=str, metavar='',
                    help='your password')

# * mutually exclusive arguments verbose and quiet
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true',
                   help='print no additional messages')
group.add_argument('-v', '--verbose', action='store_true',
                   help='print verbose output')

# * parse the arguments
args = parser.parse_args()

# * Display banner
if args.banner:
    bannerArt = pyfiglet.figlet_format(
        'blackh0le', font='ogre')
    print(bannerArt + "Developer: Sangharsh" + " | " + "Version: 0.0.5")

# * Connect to the Database
connector = _mysql.connect(
    host='localhost', user='sangharsh', passwd='sethDg@mer007', db='password_manager')


# * adding userid and password to database
def addAccount(uname, pword, usite):
    userInputUsername = uname
    userInputPassword = pword
    userInputSite = usite
    addAccountQuery = f"INSERT INTO passwordDB (username, password, site) VALUES ('{userInputUsername}', '{userInputPassword}', '{userInputSite}')"
    try:
        connector.query(addAccountQuery)
        print("Successfully Added your account")
    except _mysql.Error as error:
        print("Sorry Could not add your Account :(" + error)

# * getting password from database
def retrievePassword(usite):
    userInputSite = usite
    getPasswordQuery = f"SELECT * FROM passwordDB WHERE site = '{userInputSite}'"
    try:
        connector.query(getPasswordQuery)
        result = connector.store_result()
        results = result.fetch_row(maxrows=0, how=1)
    except _mysql.Error as error:
        print("Sorry I could not get your Password :(" + error)
    return results


# * Execute required function
finalResult = {}
if args.mode == 'get':
    finalResult = retrievePassword(args.site)

if args.mode == 'add':
    addAccount(args.username, args.password, args.site)

# * Display output
if args.mode == 'get':
    if args.quiet:
        print(f"USERNAME :: {finalResult[0]['username'].decode()}")
        print(f"PASSWORD :: {finalResult[0]['password'].decode()}")
    elif args.verbose:
        print(f"USERNAME IS -> {finalResult[0]['username'].decode('UTF-8')}")
        print(f"PASSWORD IS -> {finalResult[0]['password'].decode('UTF-8')}")
    else:
        pass
