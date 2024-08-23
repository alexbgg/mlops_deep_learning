from fastapi import FastAPI, Depends
from .auth.authentication import router as auth_router
from .endpoints.prediction import router as predict_router
from .endpoints.ab_testing import router as ab_testing_router
from .endpoints.retrain import router as retrain_router
from .endpoints.collect_data import router as collect_data_router
from .endpoints.api_request_log import router as api_request_log_router
from .endpoints.error_log import router as error_log_router
from .endpoints.model_metadata import router as model_metadata_router

from .auth.auth_utils import get_current_user

app = FastAPI()


from .database.db import Base, engine
Base.metadata.create_all(bind=engine)


# Include routers for different functionalities
app.include_router(auth_router, tags=["Authentication"])
app.include_router(predict_router, tags=["Prediction"])
app.include_router(ab_testing_router, tags=["AB Testing"])
app.include_router(api_request_log_router, tags=["API Request Log"])
app.include_router(error_log_router, tags=["Error Log"])
app.include_router(model_metadata_router, tags=["Model Metadata"])
app.include_router(collect_data_router, tags=["Collecting Data"])
app.include_router(retrain_router, tags=["Retrain"])

@app.get("/")
def read_root():
     return {"message": "Welcome to the Plant Detection API!"}

