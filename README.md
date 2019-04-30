# donut

The purpose of this script is to update dot files somewhere.  It works in the
following way.  Two locations are set:

- `dothome`, absolute path to the set the dotfiles
- `dotarchive`, absolute path to the dot files (usually some git archive)

Then symlinks are made from dothome to dotarchive.  Simple as that.

## Installation

```
pip install donut
```

## Usage

Example
```
donut ~ ~/repos/dotfiles
```

Help
```
usage: donut [-h] [--verbose] dothome dotarchive

positional arguments:
  dothome     absolute path to the dotfiles
  dotarchive  absolute path to the dotfile archive

optional arguments:
  -h, --help  show this help message and exit
  --verbose   verbose mode
```

## Notes

- `setup.cfg` should be a flat list of files in `dotarchive`
  - if `setup.cfg` exists, then only the files in `setup.cfg` are linked
  - else if `setup.cfg` does not exist, then all files in `dotarchive` are (attempted to be) linked
- the symlinking is passive by default, and non-destructive even if forced
  - `.dotfiles-original/` is created.  Any existing files will be moved here if a forced symlink is requested
