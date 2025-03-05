from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2AuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[Fido2AuthenticationMethodConfiguration]] = Field(default=None,alias="value",)

from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration

