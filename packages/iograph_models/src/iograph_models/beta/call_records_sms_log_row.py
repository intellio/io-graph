from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsSmsLogRow(BaseModel):
	administrativeUnitInfos: Optional[list[CallRecordsAdministrativeUnitInfo]] = Field(alias="administrativeUnitInfos",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	otherPartyCountryCode: Optional[str] = Field(alias="otherPartyCountryCode",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callCharge: Optional[int] = Field(alias="callCharge",default=None,)
	currency: Optional[str] = Field(alias="currency",default=None,)
	destinationContext: Optional[str] = Field(alias="destinationContext",default=None,)
	destinationName: Optional[str] = Field(alias="destinationName",default=None,)
	destinationNumber: Optional[str] = Field(alias="destinationNumber",default=None,)
	licenseCapability: Optional[str] = Field(alias="licenseCapability",default=None,)
	sentDateTime: Optional[datetime] = Field(alias="sentDateTime",default=None,)
	smsId: Optional[str] = Field(alias="smsId",default=None,)
	smsType: Optional[str] = Field(alias="smsType",default=None,)
	smsUnits: Optional[int] = Field(alias="smsUnits",default=None,)
	sourceNumber: Optional[str] = Field(alias="sourceNumber",default=None,)
	tenantCountryCode: Optional[str] = Field(alias="tenantCountryCode",default=None,)
	userCountryCode: Optional[str] = Field(alias="userCountryCode",default=None,)

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo

