from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Complete_signupPostRequest(BaseModel):
	enterpriseToken: Optional[str] = Field(alias="enterpriseToken", default=None,)

