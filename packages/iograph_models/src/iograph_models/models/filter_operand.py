from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FilterOperand(BaseModel):
	values: list[Optional[str]] = Field(alias="values",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


