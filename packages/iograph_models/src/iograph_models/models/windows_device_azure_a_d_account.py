from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDeviceAzureADAccount(BaseModel):
	password: Optional[str] = Field(alias="password",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)


