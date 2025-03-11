from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessIpRange(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	beginAddress: Optional[str] = Field(alias="beginAddress",default=None,)
	endAddress: Optional[str] = Field(alias="endAddress",default=None,)


