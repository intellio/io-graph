from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExtendRemoteHelpSessionResponse(BaseModel):
	acsHelperUserToken: Optional[str] = Field(alias="acsHelperUserToken", default=None,)
	pubSubHelperAccessUri: Optional[str] = Field(alias="pubSubHelperAccessUri", default=None,)
	sessionExpirationDateTime: Optional[datetime] = Field(alias="sessionExpirationDateTime", default=None,)
	sessionKey: Optional[str] = Field(alias="sessionKey", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


