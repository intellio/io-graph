from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySslCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.sslCertificate"] = Field(alias="@odata.type", default="#microsoft.graph.security.sslCertificate")
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	fingerprint: Optional[str] = Field(alias="fingerprint", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	issueDateTime: Optional[datetime] = Field(alias="issueDateTime", default=None,)
	issuer: Optional[SecuritySslCertificateEntity] = Field(alias="issuer", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	sha1: Optional[str] = Field(alias="sha1", default=None,)
	subject: Optional[SecuritySslCertificateEntity] = Field(alias="subject", default=None,)
	relatedHosts: Optional[list[Annotated[Union[SecurityHostname, SecurityIpAddress]],Field(discriminator="odata_type")]]] = Field(alias="relatedHosts", default=None,)

from .security_ssl_certificate_entity import SecuritySslCertificateEntity
from .security_ssl_certificate_entity import SecuritySslCertificateEntity
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress

