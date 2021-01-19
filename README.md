# S3cure
Stupid python based password manager (CLI)

## Installation

Install the dependencies using

```bash
pip install -r requirements.txt
```

## Usage

```bash
$ ./main.py -h
usage: main.py [-h] [-s] [-b] [-m] [-u] [-p] [-q | -v]

A simple Password Manager

optional arguments:
  -h, --help        show this help message and exit
  -s , --site       The website you want to retrieve credentials for
  -b, --banner      display banner
  -m , --mode       Speficy operation mode, add for entry or get for retrieval
  -u , --username   your username or email
  -p , --password   your password
  -q, --quiet       print no additional messages
  -v, --verbose     print verbose output
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
