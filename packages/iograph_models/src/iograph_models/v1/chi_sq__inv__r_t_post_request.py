from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Chi_sq__inv__r_tPostRequest(BaseModel):
	probability: Optional[str] = Field(alias="probability", default=None,)
	degFreedom: Optional[str] = Field(alias="degFreedom", default=None,)

