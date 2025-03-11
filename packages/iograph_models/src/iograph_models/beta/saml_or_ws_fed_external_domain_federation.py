from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SamlOrWsFedExternalDomainFederation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	issuerUri: Optional[str] = Field(alias="issuerUri",default=None,)
	metadataExchangeUri: Optional[str] = Field(alias="metadataExchangeUri",default=None,)
	passiveSignInUri: Optional[str] = Field(alias="passiveSignInUri",default=None,)
	preferredAuthenticationProtocol: Optional[AuthenticationProtocol | str] = Field(alias="preferredAuthenticationProtocol",default=None,)
	signingCertificate: Optional[str] = Field(alias="signingCertificate",default=None,)
	domains: Optional[list[ExternalDomainName]] = Field(alias="domains",default=None,)

from .authentication_protocol import AuthenticationProtocol
from .external_domain_name import ExternalDomainName

