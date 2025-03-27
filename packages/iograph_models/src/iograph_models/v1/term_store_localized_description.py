from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermStoreLocalizedDescription(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


