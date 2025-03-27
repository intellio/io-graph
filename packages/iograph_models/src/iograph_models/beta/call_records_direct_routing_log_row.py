from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsDirectRoutingLogRow(BaseModel):
	administrativeUnitInfos: Optional[list[CallRecordsAdministrativeUnitInfo]] = Field(alias="administrativeUnitInfos", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	otherPartyCountryCode: Optional[str] = Field(alias="otherPartyCountryCode", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	calleeNumber: Optional[str] = Field(alias="calleeNumber", default=None,)
	callEndSubReason: Optional[int] = Field(alias="callEndSubReason", default=None,)
	callerNumber: Optional[str] = Field(alias="callerNumber", default=None,)
	callType: Optional[str] = Field(alias="callType", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	duration: Optional[int] = Field(alias="duration", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	failureDateTime: Optional[datetime] = Field(alias="failureDateTime", default=None,)
	finalSipCode: Optional[int] = Field(alias="finalSipCode", default=None,)
	finalSipCodePhrase: Optional[str] = Field(alias="finalSipCodePhrase", default=None,)
	inviteDateTime: Optional[datetime] = Field(alias="inviteDateTime", default=None,)
	mediaBypassEnabled: Optional[bool] = Field(alias="mediaBypassEnabled", default=None,)
	mediaPathLocation: Optional[str] = Field(alias="mediaPathLocation", default=None,)
	signalingLocation: Optional[str] = Field(alias="signalingLocation", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	successfulCall: Optional[bool] = Field(alias="successfulCall", default=None,)
	transferorCorrelationId: Optional[str] = Field(alias="transferorCorrelationId", default=None,)
	trunkFullyQualifiedDomainName: Optional[str] = Field(alias="trunkFullyQualifiedDomainName", default=None,)
	userCountryCode: Optional[str] = Field(alias="userCountryCode", default=None,)

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo

