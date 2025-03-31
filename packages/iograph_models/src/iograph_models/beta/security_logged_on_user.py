from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityLoggedOnUser(BaseModel):
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

