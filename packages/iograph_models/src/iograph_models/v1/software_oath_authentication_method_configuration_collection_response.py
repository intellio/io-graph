from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SoftwareOathAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SoftwareOathAuthenticationMethodConfiguration]] = Field(alias="value",default=None,)

from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration

