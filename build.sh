pyinstaller -F lazyrun.py
cd dist
staticx lazyrun ../lazyrun
cd ..
chmod a+x lazyrun
rm -rf build dist lazyrun.spec __pycache__

