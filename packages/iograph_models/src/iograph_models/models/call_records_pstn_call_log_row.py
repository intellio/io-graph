from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsPstnCallLogRow(BaseModel):
	callDurationSource: Optional[CallRecordsPstnCallDurationSource] = Field(default=None,alias="callDurationSource",)
	calleeNumber: Optional[str] = Field(default=None,alias="calleeNumber",)
	callerNumber: Optional[str] = Field(default=None,alias="callerNumber",)
	callId: Optional[str] = Field(default=None,alias="callId",)
	callType: Optional[str] = Field(default=None,alias="callType",)
	charge: Optional[int] = Field(default=None,alias="charge",)
	conferenceId: Optional[str] = Field(default=None,alias="conferenceId",)
	connectionCharge: Optional[int] = Field(default=None,alias="connectionCharge",)
	currency: Optional[str] = Field(default=None,alias="currency",)
	destinationContext: Optional[str] = Field(default=None,alias="destinationContext",)
	destinationName: Optional[str] = Field(default=None,alias="destinationName",)
	duration: Optional[int] = Field(default=None,alias="duration",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	id: Optional[str] = Field(default=None,alias="id",)
	inventoryType: Optional[str] = Field(default=None,alias="inventoryType",)
	licenseCapability: Optional[str] = Field(default=None,alias="licenseCapability",)
	operator: Optional[str] = Field(default=None,alias="operator",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	tenantCountryCode: Optional[str] = Field(default=None,alias="tenantCountryCode",)
	usageCountryCode: Optional[str] = Field(default=None,alias="usageCountryCode",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_pstn_call_duration_source import CallRecordsPstnCallDurationSource

