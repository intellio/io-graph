from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LocaleInfo(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


