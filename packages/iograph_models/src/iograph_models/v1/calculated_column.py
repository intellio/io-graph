from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CalculatedColumn(BaseModel):
	format: Optional[str] = Field(alias="format", default=None,)
	formula: Optional[str] = Field(alias="formula", default=None,)
	outputType: Optional[str] = Field(alias="outputType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

