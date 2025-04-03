from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPCConnectivityIssue(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPCConnectivityIssue"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPCConnectivityIssue")
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	errorCode: Optional[str] = Field(alias="errorCode", default=None,)
	errorDateTime: Optional[datetime] = Field(alias="errorDateTime", default=None,)
	errorDescription: Optional[str] = Field(alias="errorDescription", default=None,)
	recommendedAction: Optional[str] = Field(alias="recommendedAction", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

