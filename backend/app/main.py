from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.database import db
from .routes.search import router as search_router
from .routes.admin import router as admin_router

app = FastAPI(title="Banker API", version="1.0.0")

# ----------------------------
# CORS SETTINGS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(search_router)
app.include_router(admin_router)

@app.get("/api/health")
async def health():
    return {"status": "ok"}
