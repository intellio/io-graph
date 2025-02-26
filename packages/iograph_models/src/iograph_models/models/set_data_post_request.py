from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_dataPostRequest(BaseModel):
	sourceData: Optional[str] = Field(default=None,alias="sourceData",)
	seriesBy: Optional[str] = Field(default=None,alias="seriesBy",)


