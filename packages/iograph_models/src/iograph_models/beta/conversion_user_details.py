from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConversionUserDetails(BaseModel):
	convertedToInternalUserDateTime: Optional[datetime] = Field(alias="convertedToInternalUserDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	mail: Optional[str] = Field(alias="mail",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


