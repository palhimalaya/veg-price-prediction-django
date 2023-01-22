echo "Building project"
pip install -r requirements.txt
python3.6 manage.py collectstatic
echo "Build end"