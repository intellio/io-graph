from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class F__invPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	degFreedom1: Optional[str] = Field(default=None,alias="degFreedom1",)
	degFreedom2: Optional[str] = Field(default=None,alias="degFreedom2",)


