from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OpenIdConnectIdentityProviderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OpenIdConnectIdentityProvider]] = Field(alias="value", default=None,)

from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider

