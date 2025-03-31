from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[X509CertificateAuthenticationMethodConfiguration]] = Field(alias="value", default=None,)

from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
