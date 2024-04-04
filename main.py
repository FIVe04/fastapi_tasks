from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables

from router import router as tasks_router

import uvicorn

import ssl

import sys



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("DB droppped and ready")
    yield
    print("Turning off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

# if __name__ == "__main__":
#     # if len(sys.argv) == 3:
#     #     ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#     #     ssl_context.load_cert_chain(sys.argv[1], keyfile=sys.argv[2])
#     #     uvicorn.run(app, host="0.0.0.0", port=80, ssl=ssl_context)
#     # else:
#     uvicorn.run(app, host="0.0.0.0", port=80)





