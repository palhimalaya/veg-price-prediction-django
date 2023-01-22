echo "Building project"
python3.9 -m pip install -r requirements.txt
python3.9 -m manage.py collectstatic --noinput --clear

echo "Build end"