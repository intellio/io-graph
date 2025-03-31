from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ActivatePostRequest(BaseModel):
	verificationCode: Optional[str] = Field(alias="verificationCode", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

