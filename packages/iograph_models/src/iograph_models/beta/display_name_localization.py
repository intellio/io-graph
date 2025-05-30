from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DisplayNameLocalization(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

