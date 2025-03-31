from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInStatus(BaseModel):
	additionalDetails: Optional[str] = Field(alias="additionalDetails", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	failureReason: Optional[str] = Field(alias="failureReason", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

