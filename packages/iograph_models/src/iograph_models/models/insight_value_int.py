from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InsightValueInt(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: Optional[int] = Field(default=None,alias="value",)


