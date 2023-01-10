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
docker-compose build
docker-compose run web alembic upgrade head
docker-compose run web alembic revision --autogenerate -m "table migration"
docker-compose up
```
