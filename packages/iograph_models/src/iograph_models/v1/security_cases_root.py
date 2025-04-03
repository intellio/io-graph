from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCasesRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.casesRoot"] = Field(alias="@odata.type", default="#microsoft.graph.security.casesRoot")
	ediscoveryCases: Optional[list[SecurityEdiscoveryCase]] = Field(alias="ediscoveryCases", default=None,)

from .security_ediscovery_case import SecurityEdiscoveryCase
