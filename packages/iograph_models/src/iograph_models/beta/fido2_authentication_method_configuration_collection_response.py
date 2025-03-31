from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Fido2AuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Fido2AuthenticationMethodConfiguration]] = Field(alias="value", default=None,)

from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
