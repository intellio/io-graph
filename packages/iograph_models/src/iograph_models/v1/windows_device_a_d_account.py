from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDeviceADAccount(BaseModel):
	password: Optional[str] = Field(alias="password",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	domainName: Optional[str] = Field(alias="domainName",default=None,)
	userName: Optional[str] = Field(alias="userName",default=None,)


