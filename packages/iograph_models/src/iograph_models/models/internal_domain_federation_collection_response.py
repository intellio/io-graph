from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InternalDomainFederationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[InternalDomainFederation] = Field(alias="value",)

from .internal_domain_federation import InternalDomainFederation

