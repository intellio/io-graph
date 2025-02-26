from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UrlAssessmentRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UrlAssessmentRequest] = Field(alias="value",)

from .url_assessment_request import UrlAssessmentRequest

