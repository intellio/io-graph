from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IPv4Range(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lowerAddress: Optional[str] = Field(alias="lowerAddress",default=None,)
	upperAddress: Optional[str] = Field(alias="upperAddress",default=None,)


