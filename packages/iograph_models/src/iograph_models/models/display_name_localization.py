from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DisplayNameLocalization(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


