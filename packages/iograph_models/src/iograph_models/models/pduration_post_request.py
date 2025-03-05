from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PdurationPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	fv: Optional[str] = Field(default=None,alias="fv",)


