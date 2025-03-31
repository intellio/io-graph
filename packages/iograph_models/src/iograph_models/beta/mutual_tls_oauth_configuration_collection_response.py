from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MutualTlsOauthConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MutualTlsOauthConfiguration]] = Field(alias="value", default=None,)

from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
