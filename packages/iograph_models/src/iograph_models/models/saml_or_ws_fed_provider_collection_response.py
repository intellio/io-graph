from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SamlOrWsFedProviderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[SamlOrWsFedProvider]]] = Field(alias="value",default=None,)

from .saml_or_ws_fed_provider import SamlOrWsFedProvider

