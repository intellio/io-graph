from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermStoreLocalizedLabel(BaseModel):
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


