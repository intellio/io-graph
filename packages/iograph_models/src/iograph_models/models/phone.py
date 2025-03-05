from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Phone(BaseModel):
	language: Optional[str] = Field(default=None,alias="language",)
	number: Optional[str] = Field(default=None,alias="number",)
	region: Optional[str] = Field(default=None,alias="region",)
	type: Optional[PhoneType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .phone_type import PhoneType

