from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IntegerRange(BaseModel):
	end: Optional[int] = Field(default=None,alias="end",)
	start: Optional[int] = Field(default=None,alias="start",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


