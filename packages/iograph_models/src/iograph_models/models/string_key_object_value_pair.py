from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StringKeyObjectValuePair(BaseModel):
	key: Optional[str] = Field(default=None,alias="key",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


