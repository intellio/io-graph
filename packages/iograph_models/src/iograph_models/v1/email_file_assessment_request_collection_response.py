from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmailFileAssessmentRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EmailFileAssessmentRequest]] = Field(alias="value", default=None,)

from .email_file_assessment_request import EmailFileAssessmentRequest

