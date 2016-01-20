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
import os


def make_symlinks(dothome, dotarchive, dotfiles):
    pass


def get_dotfiles_list(dotarchive):
    """
    Attempt to find a list of files in setup.cfg

    If not, just grab the files in dotarchive
    """
    cfg_file = os.path.join(dotarchive, 'setup.cfg')
    dotfiles = []

    if os.path.isfile(cfg_file):
        try:
            with open(cfg_file) as f:
                dotfiles = f.readlines()
        except:
            raise EnvironmentError('could not read %s' % cfg_file)

        dotfiles = [d.strip() for d in dotfiles]
    else:
        dotfiles = [f for f in os.listdir(dotarchive)]

    return dotfiles


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

    dotfiles = get_dotfiles_list(args.dotarchive)
    print(dotfiles)

    make_symlinks(args.dothome, args.dotarchive, dotfiles)

if __name__ == "__main__":
    main()
