from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OidcIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.oidcIdentityProvider"] = Field(alias="@odata.type", default="#microsoft.graph.oidcIdentityProvider")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	clientAuthentication: Optional[Union[OidcClientSecretAuthentication, OidcPrivateJwtKeyClientAuthentication]] = Field(alias="clientAuthentication", default=None,discriminator="odata_type", )
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	inboundClaimMapping: Optional[OidcInboundClaimMappingOverride] = Field(alias="inboundClaimMapping", default=None,)
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	responseType: Optional[OidcResponseType | str] = Field(alias="responseType", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)
	wellKnownEndpoint: Optional[str] = Field(alias="wellKnownEndpoint", default=None,)

from .oidc_client_secret_authentication import OidcClientSecretAuthentication
from .oidc_private_jwt_key_client_authentication import OidcPrivateJwtKeyClientAuthentication
from .oidc_inbound_claim_mapping_override import OidcInboundClaimMappingOverride
from .oidc_response_type import OidcResponseType

