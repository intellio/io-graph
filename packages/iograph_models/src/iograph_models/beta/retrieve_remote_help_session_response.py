from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RetrieveRemoteHelpSessionResponse(BaseModel):
	acsGroupId: Optional[str] = Field(alias="acsGroupId",default=None,)
	acsHelperUserId: Optional[str] = Field(alias="acsHelperUserId",default=None,)
	acsHelperUserToken: Optional[str] = Field(alias="acsHelperUserToken",default=None,)
	acsSharerUserId: Optional[str] = Field(alias="acsSharerUserId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	pubSubGroupId: Optional[str] = Field(alias="pubSubGroupId",default=None,)
	pubSubHelperAccessUri: Optional[str] = Field(alias="pubSubHelperAccessUri",default=None,)
	sessionExpirationDateTime: Optional[datetime] = Field(alias="sessionExpirationDateTime",default=None,)
	sessionKey: Optional[str] = Field(alias="sessionKey",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


