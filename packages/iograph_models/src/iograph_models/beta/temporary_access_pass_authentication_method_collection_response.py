from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TemporaryAccessPassAuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TemporaryAccessPassAuthenticationMethod]] = Field(alias="value", default=None,)

from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
