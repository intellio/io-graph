from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Accr_int_mPostRequest(BaseModel):
	issue: Optional[str] = Field(default=None,alias="issue",)
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	par: Optional[str] = Field(default=None,alias="par",)
	basis: Optional[str] = Field(default=None,alias="basis",)


