from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterOperand(BaseModel):
	values: Optional[list[str]] = Field(default=None,alias="values",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


