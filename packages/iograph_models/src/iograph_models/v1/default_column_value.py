from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultColumnValue(BaseModel):
	formula: Optional[str] = Field(alias="formula", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

