from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WipePostRequest(BaseModel):
	keepEnrollmentData: Optional[bool] = Field(default=None,alias="keepEnrollmentData",)
	keepUserData: Optional[bool] = Field(default=None,alias="keepUserData",)
	macOsUnlockCode: Optional[str] = Field(default=None,alias="macOsUnlockCode",)
	persistEsimDataPlan: Optional[bool] = Field(default=None,alias="persistEsimDataPlan",)


