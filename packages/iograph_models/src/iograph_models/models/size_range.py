from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SizeRange(BaseModel):
	maximumSize: Optional[int] = Field(default=None,alias="maximumSize",)
	minimumSize: Optional[int] = Field(default=None,alias="minimumSize",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


