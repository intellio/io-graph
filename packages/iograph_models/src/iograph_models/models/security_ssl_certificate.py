from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySslCertificate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	fingerprint: Optional[str] = Field(alias="fingerprint",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	issueDateTime: Optional[datetime] = Field(alias="issueDateTime",default=None,)
	issuer: Optional[SecuritySslCertificateEntity] = Field(alias="issuer",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber",default=None,)
	sha1: Optional[str] = Field(alias="sha1",default=None,)
	subject: Optional[SecuritySslCertificateEntity] = Field(alias="subject",default=None,)
	relatedHosts: SerializeAsAny[Optional[list[SecurityHost]]] = Field(alias="relatedHosts",default=None,)

from .security_ssl_certificate_entity import SecuritySslCertificateEntity
from .security_ssl_certificate_entity import SecuritySslCertificateEntity
from .security_host import SecurityHost

