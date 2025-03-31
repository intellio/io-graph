from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationFailureCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AuthenticationFailure]] = Field(alias="value", default=None,)

from .authentication_failure import AuthenticationFailure
