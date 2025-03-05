from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsDirectRoutingLogRow(BaseModel):
	calleeNumber: Optional[str] = Field(default=None,alias="calleeNumber",)
	callEndSubReason: Optional[int] = Field(default=None,alias="callEndSubReason",)
	callerNumber: Optional[str] = Field(default=None,alias="callerNumber",)
	callType: Optional[str] = Field(default=None,alias="callType",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	duration: Optional[int] = Field(default=None,alias="duration",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	failureDateTime: Optional[datetime] = Field(default=None,alias="failureDateTime",)
	finalSipCode: Optional[int] = Field(default=None,alias="finalSipCode",)
	finalSipCodePhrase: Optional[str] = Field(default=None,alias="finalSipCodePhrase",)
	id: Optional[str] = Field(default=None,alias="id",)
	inviteDateTime: Optional[datetime] = Field(default=None,alias="inviteDateTime",)
	mediaBypassEnabled: Optional[bool] = Field(default=None,alias="mediaBypassEnabled",)
	mediaPathLocation: Optional[str] = Field(default=None,alias="mediaPathLocation",)
	signalingLocation: Optional[str] = Field(default=None,alias="signalingLocation",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	successfulCall: Optional[bool] = Field(default=None,alias="successfulCall",)
	trunkFullyQualifiedDomainName: Optional[str] = Field(default=None,alias="trunkFullyQualifiedDomainName",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


