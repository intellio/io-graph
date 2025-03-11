from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharedAppleDeviceUser(BaseModel):
	dataQuota: Optional[int] = Field(alias="dataQuota",default=None,)
	dataToSync: Optional[bool] = Field(alias="dataToSync",default=None,)
	dataUsed: Optional[int] = Field(alias="dataUsed",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


