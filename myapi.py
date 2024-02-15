"""module to implement fast api"""

from fastapi import FastAPI, status, HTTPException
import mychromadb

app = FastAPI()


@app.get("/")
async def root():
    """api function for root path"""
    return "Welcome to my Q&A application"


@app.post(
    "/upload/{pdf_path}/{pdf_name}",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
)
async def upload_docs(pdf_path: str, pdf_name: str):
    """
    for uploading files
    ### example pdf path: "C:\\Users\\promact\\Downloads\\bear_story.pdf"
    ### example pdf name: bear_story
    """
    try:
        mychromadb.embed_document(file_path=pdf_path, file_name=pdf_name)
        db = mychromadb.get_db()
        docs = db.get(where={"file_name": pdf_name})
        response_data = {"message": "File uploaded successfully", "file": pdf_name, "content": docs}
        return response_data

    except Exception as e:
        raise HTTPException(
            status_code=500, detail="error in uploading file"
        ) from e


@app.get("/answers/{pdf_name}/{question}", status_code=status.HTTP_200_OK)
async def get_answers(pdf_name: str, question: str):
    """
    for asking question answers
    ### example: pdf_name = bear_story
    ###          question = "what the bear said at the end?"   
    """
    try:
        ans = mychromadb.get_answer_from_palm2(question, pdf_name)
        return ans

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="internal server error"
        ) from e
