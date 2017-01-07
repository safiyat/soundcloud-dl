#
#
#
#
#
#

import argparse
import requests
from requests.compat import urljoin, quote_plus
import sys

BASE_URL='https://soundcloud.com/'


def get_parser():
    parser = argparse.ArgumentParser(
        prog='sdcloud-dl', description='Downloads the track(s) from SoundCloud '
                                       'that are publicly accessible.')
    parser.add_argument('-a', '--artist')
    return parser


def get_info(args):
    if args.artist:
        url = urljoin(BASE_URL, '%s/tracks' % args.artist)



def main():
    """The main method. The entry-point."""
    parser = get_parser()
    args = parser.parse_args()


if __name__ == '__main__':
    sys.exit(main())
