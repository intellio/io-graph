from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsPstnCallLogRow(BaseModel):
	administrativeUnitInfos: Optional[list[CallRecordsAdministrativeUnitInfo]] = Field(alias="administrativeUnitInfos", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	otherPartyCountryCode: Optional[str] = Field(alias="otherPartyCountryCode", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	callDurationSource: Optional[CallRecordsPstnCallDurationSource | str] = Field(alias="callDurationSource", default=None,)
	calleeNumber: Optional[str] = Field(alias="calleeNumber", default=None,)
	callerNumber: Optional[str] = Field(alias="callerNumber", default=None,)
	callId: Optional[str] = Field(alias="callId", default=None,)
	callType: Optional[str] = Field(alias="callType", default=None,)
	charge: Optional[int] = Field(alias="charge", default=None,)
	clientLocalIpV4Address: Optional[str] = Field(alias="clientLocalIpV4Address", default=None,)
	clientLocalIpV6Address: Optional[str] = Field(alias="clientLocalIpV6Address", default=None,)
	clientPublicIpV4Address: Optional[str] = Field(alias="clientPublicIpV4Address", default=None,)
	clientPublicIpV6Address: Optional[str] = Field(alias="clientPublicIpV6Address", default=None,)
	conferenceId: Optional[str] = Field(alias="conferenceId", default=None,)
	connectionCharge: Optional[int] = Field(alias="connectionCharge", default=None,)
	currency: Optional[str] = Field(alias="currency", default=None,)
	destinationContext: Optional[str] = Field(alias="destinationContext", default=None,)
	destinationName: Optional[str] = Field(alias="destinationName", default=None,)
	duration: Optional[int] = Field(alias="duration", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	inventoryType: Optional[str] = Field(alias="inventoryType", default=None,)
	licenseCapability: Optional[str] = Field(alias="licenseCapability", default=None,)
	operator: Optional[str] = Field(alias="operator", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	tenantCountryCode: Optional[str] = Field(alias="tenantCountryCode", default=None,)
	usageCountryCode: Optional[str] = Field(alias="usageCountryCode", default=None,)

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo
from .call_records_pstn_call_duration_source import CallRecordsPstnCallDurationSource

