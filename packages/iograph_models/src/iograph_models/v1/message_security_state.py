from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MessageSecurityState(BaseModel):
	connectingIP: Optional[str] = Field(alias="connectingIP", default=None,)
	deliveryAction: Optional[str] = Field(alias="deliveryAction", default=None,)
	deliveryLocation: Optional[str] = Field(alias="deliveryLocation", default=None,)
	directionality: Optional[str] = Field(alias="directionality", default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId", default=None,)
	messageFingerprint: Optional[str] = Field(alias="messageFingerprint", default=None,)
	messageReceivedDateTime: Optional[datetime] = Field(alias="messageReceivedDateTime", default=None,)
	messageSubject: Optional[str] = Field(alias="messageSubject", default=None,)
	networkMessageId: Optional[str] = Field(alias="networkMessageId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


