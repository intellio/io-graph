from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalculatedColumn(BaseModel):
	format: Optional[str] = Field(default=None,alias="format",)
	formula: Optional[str] = Field(default=None,alias="formula",)
	outputType: Optional[str] = Field(default=None,alias="outputType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


