from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Phone(BaseModel):
	language: Optional[str] = Field(alias="language",default=None,)
	number: Optional[str] = Field(alias="number",default=None,)
	region: Optional[str] = Field(alias="region",default=None,)
	type: Optional[str | PhoneType] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .phone_type import PhoneType

