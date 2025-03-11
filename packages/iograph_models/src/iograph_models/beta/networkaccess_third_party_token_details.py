from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessThirdPartyTokenDetails(BaseModel):
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	issuedAtDateTime: Optional[datetime] = Field(alias="issuedAtDateTime",default=None,)
	uniqueTokenIdentifier: Optional[str] = Field(alias="uniqueTokenIdentifier",default=None,)
	validFromDateTime: Optional[datetime] = Field(alias="validFromDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


