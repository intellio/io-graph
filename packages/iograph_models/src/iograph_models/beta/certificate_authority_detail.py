from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateAuthorityDetail(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	certificate: Optional[str] = Field(alias="certificate",default=None,)
	certificateAuthorityType: Optional[CertificateAuthorityType | str] = Field(alias="certificateAuthorityType",default=None,)
	certificateRevocationListUrl: Optional[str] = Field(alias="certificateRevocationListUrl",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deltaCertificateRevocationListUrl: Optional[str] = Field(alias="deltaCertificateRevocationListUrl",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	isIssuerHintEnabled: Optional[bool] = Field(alias="isIssuerHintEnabled",default=None,)
	issuer: Optional[str] = Field(alias="issuer",default=None,)
	issuerSubjectKeyIdentifier: Optional[str] = Field(alias="issuerSubjectKeyIdentifier",default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint",default=None,)

from .certificate_authority_type import CertificateAuthorityType

