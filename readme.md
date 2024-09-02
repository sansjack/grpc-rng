## gRPC Python

## local run
- install BloomRPC and import the rng.proto file
- install python (im using 3.12)
- make install
- run `make run`



## How to run docker
- install BloomRPC and import the rng.proto file
- create a .env file by copying the .env.example file
- run `make docker-run` || `docker-compose up --build -d`
- goto BloomRPC and run the function at 127.0.0.1:50051
- check postgres database random_numbers table for all the numbers that have been generated.

