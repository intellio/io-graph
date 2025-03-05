from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MessageSecurityState(BaseModel):
	connectingIP: Optional[str] = Field(default=None,alias="connectingIP",)
	deliveryAction: Optional[str] = Field(default=None,alias="deliveryAction",)
	deliveryLocation: Optional[str] = Field(default=None,alias="deliveryLocation",)
	directionality: Optional[str] = Field(default=None,alias="directionality",)
	internetMessageId: Optional[str] = Field(default=None,alias="internetMessageId",)
	messageFingerprint: Optional[str] = Field(default=None,alias="messageFingerprint",)
	messageReceivedDateTime: Optional[datetime] = Field(default=None,alias="messageReceivedDateTime",)
	messageSubject: Optional[str] = Field(default=None,alias="messageSubject",)
	networkMessageId: Optional[str] = Field(default=None,alias="networkMessageId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


