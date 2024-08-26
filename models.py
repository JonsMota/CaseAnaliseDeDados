from pydantic import BaseModel

class SurveyAnswer(BaseModel):
    id: int
    survey_id: int
    answer_data: str