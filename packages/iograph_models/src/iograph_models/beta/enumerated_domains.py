from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedDomains(BaseModel):
	rootDomains: Optional[RootDomains | str] = Field(alias="rootDomains", default=None,)
	odata_type: Literal["#microsoft.graph.enumeratedDomains"] = Field(alias="@odata.type", default="#microsoft.graph.enumeratedDomains")
	domainNames: Optional[list[str]] = Field(alias="domainNames", default=None,)

from .root_domains import RootDomains

