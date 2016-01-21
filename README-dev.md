Change __version__ in donut.py
git tag -a v0.1 -m "version 0.1"
git push origin v0.1
python setup.py register
python setup.py sdist upload
