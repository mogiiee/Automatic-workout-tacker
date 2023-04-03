from fastapi import FastAPI, File, HTTPException, UploadFile, Request, Form
import app.schemas as schemas
from fastapi.middleware.cors import CORSMiddleware
from . import ops
from fastapi.encoders import jsonable_encoder

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

mainAccount = "serviceAccount.json"


firebaseConfig = {
    "apiKey": "AIzaSyC_L7bacXhCfshzd35fJdyH_2prVU7FoeM",
    "authDomain": "ai-sight-471fa.firebaseapp.com",
    "projectId": "ai-sight-471fa",
    "storageBucket": "ai-sight-471fa.appspot.com",
    "messagingSenderId": "90293971390",
    "appId": "1:90293971390:web:04b27715f6059d448831ef",
    "measurementId": "G-14P2V3YKET",
    "serviceAccount": mainAccount,
    "databaseURL": "gs://ai-sight-471fa.appspot.com/all_screenshots/",
}


@app.get("/")
def root():
    return {"hello": "world"}


@app.post("/inserter", tags=["test"])
async def inserter(info: schemas.UserSignUp):
    encoded_info = jsonable_encoder(info)
    await ops.inserter(encoded_info)
    return (True, info)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), text_field: str = Form(...)):
    file_content = await file.read()  # Read the file's content
    file_size = len(file_content)  # Determine the file's size
    bucket = storage.bucket
    blob = bucket.blob(file.filename)
    blob.upload_from_string(file_content, content_type="image/jpeg")
    blob.make_public()
    text_dict = json.loads(text_field)
    email = text_dict["email"]
    timern = datetime.now()

    url = blob.public_url
    full_profile = await ops.find_user_email(email)
    user_pictures = full_profile["user-pictures"]
    url_dict = {"picture link": url, "date and time": timern}

    user_pictures.append(url_dict)
    ops.user_picture_updater(text_dict["email"], user_pictures)
    return responses.response(True, "course created!", url_dict)


@app.post("/start-workout")
async def start_workout():
    pass