from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[X509CertificateAuthenticationMethodConfiguration]] = Field(default=None,alias="value",)

from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

