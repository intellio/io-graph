from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class F__inv__r_tPostRequest(BaseModel):
	probability: Optional[str] = Field(alias="probability", default=None,)
	degFreedom1: Optional[str] = Field(alias="degFreedom1", default=None,)
	degFreedom2: Optional[str] = Field(alias="degFreedom2", default=None,)

