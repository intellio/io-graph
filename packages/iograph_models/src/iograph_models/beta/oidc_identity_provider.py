from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OidcIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	clientAuthentication: SerializeAsAny[Optional[OidcClientAuthentication]] = Field(alias="clientAuthentication",default=None,)
	clientId: Optional[str] = Field(alias="clientId",default=None,)
	inboundClaimMapping: Optional[OidcInboundClaimMappingOverride] = Field(alias="inboundClaimMapping",default=None,)
	issuer: Optional[str] = Field(alias="issuer",default=None,)
	responseType: Optional[OidcResponseType | str] = Field(alias="responseType",default=None,)
	scope: Optional[str] = Field(alias="scope",default=None,)
	wellKnownEndpoint: Optional[str] = Field(alias="wellKnownEndpoint",default=None,)

from .oidc_client_authentication import OidcClientAuthentication
from .oidc_inbound_claim_mapping_override import OidcInboundClaimMappingOverride
from .oidc_response_type import OidcResponseType

