from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IPv6CidrRange(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cidrAddress: Optional[str] = Field(alias="cidrAddress",default=None,)


