from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecuritySubmissionAdminReview(BaseModel):
	reviewBy: Optional[str] = Field(alias="reviewBy", default=None,)
	reviewDateTime: Optional[datetime] = Field(alias="reviewDateTime", default=None,)
	reviewResult: Optional[SecuritySubmissionResultCategory | str] = Field(alias="reviewResult", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_submission_result_category import SecuritySubmissionResultCategory
