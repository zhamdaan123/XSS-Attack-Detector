from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from src.detector import XSSDetector


api = APIRouter(prefix="/api", tags=['API'])


class DataModel(BaseModel):
    content: str


class MultipleDataModel(DataModel):
    label: str


class ResultModel(BaseModel):
    label: str = None
    is_malicious: bool
    score: float


@api.post('/check', response_model=ResultModel)
def check(data: DataModel):
    """API to check for malicious content"""
    try:
        detector = XSSDetector()
        is_malicious, score = detector.predict(data.content)
        return ResultModel(is_malicious=is_malicious, score=score)

    except Exception as e:
        raise HTTPException(status_code=400,
                            detail=f'Failed to detect - {str(e)}') from e


@api.post('/check/multiple', response_model=list[ResultModel])
def check(data: list[MultipleDataModel]):
    """API to check for malicious multiple content"""

    try:
        detector = XSSDetector()
        result = []
        for item in data:
            is_malicious, score = detector.predict(item.content)
            result.append(ResultModel(label=item.label,
                                      is_malicious=is_malicious,
                                      score=score))
        return result

    except Exception as e:
        raise HTTPException(status_code=400,
                            detail=f'Failed to detect - {str(e)}') from e
