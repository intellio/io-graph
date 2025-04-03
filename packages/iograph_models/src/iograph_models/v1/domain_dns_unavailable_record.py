from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DomainDnsUnavailableRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.domainDnsUnavailableRecord"] = Field(alias="@odata.type", default="#microsoft.graph.domainDnsUnavailableRecord")
	isOptional: Optional[bool] = Field(alias="isOptional", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	recordType: Optional[str] = Field(alias="recordType", default=None,)
	supportedService: Optional[str] = Field(alias="supportedService", default=None,)
	ttl: Optional[int] = Field(alias="ttl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)

