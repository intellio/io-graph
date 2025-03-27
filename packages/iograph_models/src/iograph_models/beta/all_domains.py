from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AllDomains(BaseModel):
	rootDomains: Optional[RootDomains | str] = Field(alias="rootDomains", default=None,)
	odata_type: Literal["#microsoft.graph.allDomains"] = Field(alias="@odata.type", default="#microsoft.graph.allDomains")

from .root_domains import RootDomains

