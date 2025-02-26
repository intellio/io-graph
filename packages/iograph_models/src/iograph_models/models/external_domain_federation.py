from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalDomainFederation(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	issuerUri: Optional[str] = Field(default=None,alias="issuerUri",)


