from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudCertificationAuthorityLeafCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudCertificationAuthorityLeafCertificate"] = Field(alias="@odata.type", default="#microsoft.graph.cloudCertificationAuthorityLeafCertificate")
	certificateStatus: Optional[CloudCertificationAuthorityLeafCertificateStatus | str] = Field(alias="certificateStatus", default=None,)
	certificationAuthorityIssuerUri: Optional[str] = Field(alias="certificationAuthorityIssuerUri", default=None,)
	crlDistributionPointUrl: Optional[str] = Field(alias="crlDistributionPointUrl", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	devicePlatform: Optional[str] = Field(alias="devicePlatform", default=None,)
	extendedKeyUsages: Optional[list[str]] = Field(alias="extendedKeyUsages", default=None,)
	issuerId: Optional[str] = Field(alias="issuerId", default=None,)
	issuerName: Optional[str] = Field(alias="issuerName", default=None,)
	keyUsages: Optional[list[str]] = Field(alias="keyUsages", default=None,)
	ocspResponderUri: Optional[str] = Field(alias="ocspResponderUri", default=None,)
	revocationDateTime: Optional[datetime] = Field(alias="revocationDateTime", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	subjectName: Optional[str] = Field(alias="subjectName", default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	validityEndDateTime: Optional[datetime] = Field(alias="validityEndDateTime", default=None,)
	validityStartDateTime: Optional[datetime] = Field(alias="validityStartDateTime", default=None,)

from .cloud_certification_authority_leaf_certificate_status import CloudCertificationAuthorityLeafCertificateStatus
