from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OidcInboundClaimMappingOverride(BaseModel):
	address: Optional[OidcAddressInboundClaims] = Field(alias="address",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	email_verified: Optional[str] = Field(alias="email_verified",default=None,)
	family_name: Optional[str] = Field(alias="family_name",default=None,)
	given_name: Optional[str] = Field(alias="given_name",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	phone_number: Optional[str] = Field(alias="phone_number",default=None,)
	phone_number_verified: Optional[str] = Field(alias="phone_number_verified",default=None,)
	sub: Optional[str] = Field(alias="sub",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .oidc_address_inbound_claims import OidcAddressInboundClaims

