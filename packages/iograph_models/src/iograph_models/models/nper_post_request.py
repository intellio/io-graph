from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NperPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	pmt: Optional[str] = Field(default=None,alias="pmt",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	fv: Optional[str] = Field(default=None,alias="fv",)
	type: Optional[str] = Field(default=None,alias="type",)


