from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Phone(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	type: Optional[PhoneType | str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .phone_type import PhoneType

