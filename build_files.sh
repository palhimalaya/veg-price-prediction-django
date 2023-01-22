echo "Building project"
pip install -r requirements.txt
python3.5 manage.py collectstatic
echo "Build end"