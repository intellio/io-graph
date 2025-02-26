from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationAttributeCollectionOptionConfiguration(BaseModel):
	label: Optional[str] = Field(default=None,alias="label",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


