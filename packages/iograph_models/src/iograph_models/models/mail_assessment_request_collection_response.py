from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailAssessmentRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MailAssessmentRequest] = Field(alias="value",)

from .mail_assessment_request import MailAssessmentRequest

