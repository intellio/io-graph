from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[X509CertificateAuthenticationMethodConfiguration] = Field(alias="value",)

from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

