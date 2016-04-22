# -*- coding: utf-8 -*-

"""
 Usage:
     email-permutator.py <COMPANY> <DOMAIN> <INPUT-FILE>
     email-permutator.py -h | --help
     email-permutator.py --version

 Options:
     -h --help              Show this screen
     --version              Show version
"""

from docopt import docopt
from sys import exit
import codecs
import csv


def main(args):

    try:
        input_file = codecs.open(
            args['<INPUT-FILE>'],
            'rb', encoding='utf-8',
            errors='ignore'
        )
        csv_file = codecs.open(
            'output.csv',
            'wb', encoding='utf-8',
            errors='ignore'
        )
        writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        domain = args['<DOMAIN>']

        writer.writerow(['First Name', 'Last Name', 'Position', 'Email', 'Company'])

        unique = set()

        for row in input_file.readlines():
            row = row.strip('\n\r ').lower()
            if row not in unique:
                unique.add(row)
                employee_data = row.split(' ')

                name = employee_data[0]
                second = employee_data[1]
                surname = employee_data[-1]

                permutations = []
                permutations.append('%s%s@%s' % (name, surname, domain))
                permutations.append('%s@%s' % (name, domain))
                permutations.append('%s.%s@%s' % (name, surname, domain))
                permutations.append('%s%s@%s' % (name[:1], surname, domain))
                permutations.append('%s%s@%s' % (name, surname[:1], domain))
                permutations.append('%s%s@%s' % (name[:1], surname[:1], domain))
                if second != surname:
                    permutations.append('%s%s%s@%s' % (name[:1], second[:1], surname, domain))

                for address in permutations:
                    print address
                    writer.writerow([name.capitalize(), second.capitalize(), None, address, args['<COMPANY>']])

    except Exception, e:
        print e

    finally:
        input_file.close()
        csv_file.close()


if __name__ == '__main__':
    try:
        args = docopt(__doc__, version='v1.0.0')
        main(args)
    except KeyboardInterrupt:
        print '\nAborted by user. Exiting... '
        exit(0)
