echo "Building project"
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "Build end"