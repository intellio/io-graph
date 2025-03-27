from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IpCategory(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	vendor: Optional[str] = Field(alias="vendor", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


