from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10NetworkProxyServer(BaseModel):
	address: Optional[str] = Field(alias="address",default=None,)
	exceptions: Optional[list[str]] = Field(alias="exceptions",default=None,)
	useForLocalAddresses: Optional[bool] = Field(alias="useForLocalAddresses",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


