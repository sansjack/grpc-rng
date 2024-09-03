generate:
	python -m grpc_tools.protoc -I. --python_out=src/proto --pyi_out=src/proto --grpc_python_out=src/proto rng.proto
	
run:
	python src/main.py

install:
	pip install --no-cache-dir -r requirements.txt

docker-run:
	docker-compose up --build -d