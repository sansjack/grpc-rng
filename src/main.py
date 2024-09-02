import grpc, random, logging, psycopg2

import rng_pb2_grpc
import rng_pb2
from config import Config
from concurrent import futures

PORT = "50051"
MAX_WORKERS = 4


class RandomNumber(rng_pb2_grpc.RandomNumberServiceServicer):
    def __init__(self):
        self.conn = psycopg2.connect(
            host=Config.DB_HOST,
            port=int(Config.DB_PORT),
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
        )
        self.cur = self.conn.cursor()

    def generateRandomNumber(self, request, context):
        random_number = random.randint(0, 9999)

        self.cur.execute(
            "INSERT INTO random_numbers (num) VALUES (%s)", (random_number,)
        )
        self.conn.commit()

        return rng_pb2.RandomNumberReply(number=random_number)


def main():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    rng_pb2_grpc.add_RandomNumberServiceServicer_to_server(RandomNumber(), server)

    server.add_insecure_port(f"[::]:{PORT}")
    server.start()

    print(f"Server started, listening on {PORT}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    main()
