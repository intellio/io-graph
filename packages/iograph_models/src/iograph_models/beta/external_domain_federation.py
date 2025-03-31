from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalDomainFederation(BaseModel):
	odata_type: Literal["#microsoft.graph.externalDomainFederation"] = Field(alias="@odata.type", default="#microsoft.graph.externalDomainFederation")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	issuerUri: Optional[str] = Field(alias="issuerUri", default=None,)

