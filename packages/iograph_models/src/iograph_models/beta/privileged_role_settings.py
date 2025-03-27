from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedRoleSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	approvalOnElevation: Optional[bool] = Field(alias="approvalOnElevation", default=None,)
	approverIds: Optional[list[str]] = Field(alias="approverIds", default=None,)
	elevationDuration: Optional[str] = Field(alias="elevationDuration", default=None,)
	isMfaOnElevationConfigurable: Optional[bool] = Field(alias="isMfaOnElevationConfigurable", default=None,)
	lastGlobalAdmin: Optional[bool] = Field(alias="lastGlobalAdmin", default=None,)
	maxElavationDuration: Optional[str] = Field(alias="maxElavationDuration", default=None,)
	mfaOnElevation: Optional[bool] = Field(alias="mfaOnElevation", default=None,)
	minElevationDuration: Optional[str] = Field(alias="minElevationDuration", default=None,)
	notificationToUserOnElevation: Optional[bool] = Field(alias="notificationToUserOnElevation", default=None,)
	ticketingInfoOnElevation: Optional[bool] = Field(alias="ticketingInfoOnElevation", default=None,)


