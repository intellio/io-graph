from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermStoreLocalizedName(BaseModel):
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

