from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SamlOrWsFedProviderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SamlOrWsFedProvider] = Field(alias="value",)

from .saml_or_ws_fed_provider import SamlOrWsFedProvider

