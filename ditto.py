#!/usr/bin/python
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
import shutil


def vprint(string, verbose):
    if verbose:
        print('\t[ditto] %s')


def make_symlinks(dothome, dotarchive, dotfiles, verbose=False):
    """
    1. if needed, create dothome/.dotfiles-original
    2. for each dotfile:
        - check for file or directory (not a symlink)
        - if not in the backup, move to the backup
        - create a symbolic link to dotarchive
    """

    dotbackup = os.path.join(dothome, '.dotfiles-original')
    if not os.path.isdir(dotbackup):  # makes this python 2 compliant
        vprint('.dotfiles-original does not exist...making', verbose)
        try:
            os.makedirs(dotbackup)
        except:
            raise IOError('Problem making %s' % dotbackup)
    else:
        vprint('.dotfiles-original exists', verbose)


def get_dotfiles_list(dotarchive, verbose=False):
    """
    Attempt to find a list of files in setup.cfg

    If not, just grab the files in dotarchive
    """
    cfg_file = os.path.join(dotarchive, 'setup.cfg')
    dotfiles = []

    if os.path.isfile(cfg_file):
        vprint('Found setup.cfg', verbose)
        try:
            with open(cfg_file) as f:
                dotfiles = f.readlines()
            vprint('Read setup.cfg', verbose)
        except:
            raise EnvironmentError('could not read %s' % cfg_file)

        dotfiles = [d.strip() for d in dotfiles]
    else:
        dotfiles = [f for f in os.listdir(dotarchive)]

    vprint('Dotfiles are: %s' % ' '.join(dotfiles), verbose)

    return dotfiles


def main():
    """
    Parse arguments.

    Call get_dot_files_list()

    Call make_symlinks()
    """
    # import os
    # dothome = os.path.expanduser('~')
    # dotarchive = os.path.join(dothome, '.dotarchive')

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("dothome",
                        help="absolute path to the dotfiles")
    parser.add_argument("dotarchive",
                        help="absolute path to the dotfile archive")
    parser.add_argument("--verbose", default=False,
                        help="verbose mode")
    args = parser.parse_args()

    dotfiles = get_dotfiles_list(args.dotarchive, verbose=args.verbose)

    make_symlinks(args.dothome, args.dotarchive, dotfiles,
                  verbose=args.verbose)

if __name__ == "__main__":
    main()
