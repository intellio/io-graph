from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityLoggedOnUserCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityLoggedOnUser]] = Field(alias="value", default=None,)

from .security_logged_on_user import SecurityLoggedOnUser
