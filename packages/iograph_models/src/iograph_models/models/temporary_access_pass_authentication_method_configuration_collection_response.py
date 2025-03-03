from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TemporaryAccessPassAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TemporaryAccessPassAuthenticationMethodConfiguration]] = Field(default=None,alias="value",)

from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration

