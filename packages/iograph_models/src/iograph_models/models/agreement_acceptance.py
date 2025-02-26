from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AgreementAcceptance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	agreementFileId: Optional[str] = Field(default=None,alias="agreementFileId",)
	agreementId: Optional[str] = Field(default=None,alias="agreementId",)
	deviceDisplayName: Optional[str] = Field(default=None,alias="deviceDisplayName",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceOSType: Optional[str] = Field(default=None,alias="deviceOSType",)
	deviceOSVersion: Optional[str] = Field(default=None,alias="deviceOSVersion",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	recordedDateTime: Optional[datetime] = Field(default=None,alias="recordedDateTime",)
	state: Optional[AgreementAcceptanceState] = Field(default=None,alias="state",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userEmail: Optional[str] = Field(default=None,alias="userEmail",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .agreement_acceptance_state import AgreementAcceptanceState

