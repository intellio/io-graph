from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessUser(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	firstAccessDateTime: Optional[datetime] = Field(alias="firstAccessDateTime",default=None,)
	lastAccessDateTime: Optional[datetime] = Field(alias="lastAccessDateTime",default=None,)
	totalBytesReceived: Optional[int] = Field(alias="totalBytesReceived",default=None,)
	totalBytesSent: Optional[int] = Field(alias="totalBytesSent",default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType",default=None,)
	transactionCount: Optional[int] = Field(alias="transactionCount",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	userType: Optional[NetworkaccessUserType | str] = Field(alias="userType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_traffic_type import NetworkaccessTrafficType
from .networkaccess_user_type import NetworkaccessUserType

