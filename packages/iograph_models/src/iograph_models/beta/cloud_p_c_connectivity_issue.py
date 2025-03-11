from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPCConnectivityIssue(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	errorCode: Optional[str] = Field(alias="errorCode",default=None,)
	errorDateTime: Optional[datetime] = Field(alias="errorDateTime",default=None,)
	errorDescription: Optional[str] = Field(alias="errorDescription",default=None,)
	recommendedAction: Optional[str] = Field(alias="recommendedAction",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)


