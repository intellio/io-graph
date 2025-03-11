from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AllDomains(BaseModel):
	rootDomains: Optional[RootDomains | str] = Field(alias="rootDomains",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .root_domains import RootDomains

