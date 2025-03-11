from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VpnRoute(BaseModel):
	destinationPrefix: Optional[str] = Field(alias="destinationPrefix",default=None,)
	prefixSize: Optional[int] = Field(alias="prefixSize",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


