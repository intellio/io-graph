from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermStoreLocalizedDescription(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


