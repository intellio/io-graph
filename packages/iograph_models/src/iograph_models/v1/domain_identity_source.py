from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DomainIdentitySource(BaseModel):
	odata_type: Literal["#microsoft.graph.domainIdentitySource"] = Field(alias="@odata.type", default="#microsoft.graph.domainIdentitySource")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)

