from fastapi import FastAPI
from app.routes.download import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (frontend connect ke liye MUST)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production me domain daal sakta hai
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routes
app.include_router(router, prefix="/api")

# ✅ Root test route (browser ke liye)
@app.get("/")
def home():
    return {"message": "API is running 🚀"}
