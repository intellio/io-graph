from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AgreementAcceptance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	agreementFileId: Optional[str] = Field(alias="agreementFileId", default=None,)
	agreementId: Optional[str] = Field(alias="agreementId", default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceOSType: Optional[str] = Field(alias="deviceOSType", default=None,)
	deviceOSVersion: Optional[str] = Field(alias="deviceOSVersion", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	recordedDateTime: Optional[datetime] = Field(alias="recordedDateTime", default=None,)
	state: Optional[AgreementAcceptanceState | str] = Field(alias="state", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userEmail: Optional[str] = Field(alias="userEmail", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .agreement_acceptance_state import AgreementAcceptanceState

