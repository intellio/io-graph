from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OpenIdConnectIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.openIdConnectIdentityProvider"] = Field(alias="@odata.type", default="#microsoft.graph.openIdConnectIdentityProvider")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	claimsMapping: Optional[ClaimsMapping] = Field(alias="claimsMapping", default=None,)
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret", default=None,)
	domainHint: Optional[str] = Field(alias="domainHint", default=None,)
	metadataUrl: Optional[str] = Field(alias="metadataUrl", default=None,)
	responseMode: Optional[OpenIdConnectResponseMode | str] = Field(alias="responseMode", default=None,)
	responseType: Optional[OpenIdConnectResponseTypes | str] = Field(alias="responseType", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)

from .claims_mapping import ClaimsMapping
from .open_id_connect_response_mode import OpenIdConnectResponseMode
from .open_id_connect_response_types import OpenIdConnectResponseTypes
