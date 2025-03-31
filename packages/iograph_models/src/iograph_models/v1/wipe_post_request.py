from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WipePostRequest(BaseModel):
	keepEnrollmentData: Optional[bool] = Field(alias="keepEnrollmentData", default=None,)
	keepUserData: Optional[bool] = Field(alias="keepUserData", default=None,)
	macOsUnlockCode: Optional[str] = Field(alias="macOsUnlockCode", default=None,)
	persistEsimDataPlan: Optional[bool] = Field(alias="persistEsimDataPlan", default=None,)

