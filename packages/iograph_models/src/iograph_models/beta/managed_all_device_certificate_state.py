from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedAllDeviceCertificateState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedAllDeviceCertificateState"] = Field(alias="@odata.type",)
	certificateExpirationDateTime: Optional[datetime] = Field(alias="certificateExpirationDateTime", default=None,)
	certificateExtendedKeyUsages: Optional[str] = Field(alias="certificateExtendedKeyUsages", default=None,)
	certificateIssuanceDateTime: Optional[datetime] = Field(alias="certificateIssuanceDateTime", default=None,)
	certificateIssuerName: Optional[str] = Field(alias="certificateIssuerName", default=None,)
	certificateKeyUsages: Optional[int] = Field(alias="certificateKeyUsages", default=None,)
	certificateRevokeStatus: Optional[CertificateRevocationStatus | str] = Field(alias="certificateRevokeStatus", default=None,)
	certificateRevokeStatusLastChangeDateTime: Optional[datetime] = Field(alias="certificateRevokeStatusLastChangeDateTime", default=None,)
	certificateSerialNumber: Optional[str] = Field(alias="certificateSerialNumber", default=None,)
	certificateSubjectName: Optional[str] = Field(alias="certificateSubjectName", default=None,)
	certificateThumbprint: Optional[str] = Field(alias="certificateThumbprint", default=None,)
	managedDeviceDisplayName: Optional[str] = Field(alias="managedDeviceDisplayName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .certificate_revocation_status import CertificateRevocationStatus
