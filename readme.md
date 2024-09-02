## gRPC Random Number Function Using Python

# What is this?
gRPC (Google Remote Procedure Call) is an open-source framework created by Google for calling functions on remote servers.

This example, create a gRPC server using python by taking a pre-existing proto file declaration and generates us a proto file for python which we can use to create a server. We generate these python proto files by using the grpcio-tools, i have added the command, used to the `Makefile` and it can be called by running `make generate`. The server is containerised inside a docker compose network aslongside a postgres database which we use to store the random numbers after each function invocation.

In the example we use BloomRPC to call the functions and get the result, this is really just for testing. In the "real world" (production) we would use a gRPC client to call these functions which simply offloads the compute from the client to this server.. Voilà!



## How To Run Locally 🏠
- Install [BloomRPC](https://github.com/bloomrpc/bloomrpc) and import the `rng.proto` file
- Install python (im using 3.12)
- `make install`
- Run `make run`


## How To Run Dockerised 🧰
- Install [BloomRPC](https://github.com/bloomrpc/bloomrpc) and import the `rng.proto` file
- Create a `.env` file by copying the `.env.example` file
- Run `make docker-run` || `docker-compose up --build -d`

## And Finally 🎉
- Open BloomRPC and run the function at `127.0.0.1:50051` and wait for your random numbers to be generated.
- check postgres database random_numbers table for all the numbers that have been generated.


