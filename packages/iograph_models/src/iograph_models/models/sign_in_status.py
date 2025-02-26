from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInStatus(BaseModel):
	additionalDetails: Optional[str] = Field(default=None,alias="additionalDetails",)
	errorCode: Optional[int] = Field(default=None,alias="errorCode",)
	failureReason: Optional[str] = Field(default=None,alias="failureReason",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


