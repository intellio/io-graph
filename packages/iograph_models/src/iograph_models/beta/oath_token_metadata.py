from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OathTokenMetadata(BaseModel):
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	manufacturerProperties: Optional[list[KeyValue]] = Field(alias="manufacturerProperties", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	tokenType: Optional[str] = Field(alias="tokenType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .key_value import KeyValue

