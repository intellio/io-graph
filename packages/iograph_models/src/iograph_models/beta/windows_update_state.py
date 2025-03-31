from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdateState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdateState"] = Field(alias="@odata.type",)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	featureUpdateVersion: Optional[str] = Field(alias="featureUpdateVersion", default=None,)
	lastScanDateTime: Optional[datetime] = Field(alias="lastScanDateTime", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	qualityUpdateVersion: Optional[str] = Field(alias="qualityUpdateVersion", default=None,)
	status: Optional[WindowsUpdateStatus | str] = Field(alias="status", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .windows_update_status import WindowsUpdateStatus
