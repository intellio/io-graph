from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterOperand(BaseModel):
	values: Optional[list[str]] = Field(alias="values", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


