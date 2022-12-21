# Sauce Generator
Repository to generate that sauce

# Run
```
# using py 3.10.9
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn sauce_generator.main:app --reload
```

# Docker
```
docker build -t sauce_generator .
docker run -d --name my_cool_container -p 80:80 sauce_generator
```