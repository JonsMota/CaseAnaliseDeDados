from fastapi import FastAPI, HTTPException
from typing import List
from survey_api.database import get_connection
from survey_api.models import SurveyAnswer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Survey API"}

@app.get("/answers", response_model=List[SurveyAnswer])
def get_answers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, survey_id, answer_data FROM survey_data")
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        raise HTTPException(status_code=404, detail="No answers found")
    return [SurveyAnswer(id=row[0], survey_id=row[1], answer_data=row[2]) for row in rows]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
