#!/usr/local/bin/python3
"""
The purpose of this script is to update dot files somewhere.  It works in the
following way.  Two locations are set

dothome : ($HOME)
    absolute path to the set the dotfiles

dotarchive : ($HOME/.dotarchive)
    absolute path to the dot files (usually some git archive)

Then symlinks are made from dothome to dotarchive.  Simple as that.
"""


def main():
    # import os
    # dothome = os.path.expanduser('~')
    # dotarchive = os.path.join(dothome, '.dotarchive')

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("dothome",
                        help="absolute path to the dotfiles")
    parser.add_argument("dotarchive",
                        help="absolute path to the dotfile archive")
    args = parser.parse_args()

    print(args.dothome)
    print(args.dotarchive)

if __name__ == "__main__":
    main()
