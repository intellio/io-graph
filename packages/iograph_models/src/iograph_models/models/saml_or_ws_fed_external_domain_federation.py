from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SamlOrWsFedExternalDomainFederation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	issuerUri: Optional[str] = Field(default=None,alias="issuerUri",)
	metadataExchangeUri: Optional[str] = Field(default=None,alias="metadataExchangeUri",)
	passiveSignInUri: Optional[str] = Field(default=None,alias="passiveSignInUri",)
	preferredAuthenticationProtocol: Optional[AuthenticationProtocol] = Field(default=None,alias="preferredAuthenticationProtocol",)
	signingCertificate: Optional[str] = Field(default=None,alias="signingCertificate",)
	domains: Optional[list[ExternalDomainName]] = Field(default=None,alias="domains",)

from .authentication_protocol import AuthenticationProtocol
from .external_domain_name import ExternalDomainName

