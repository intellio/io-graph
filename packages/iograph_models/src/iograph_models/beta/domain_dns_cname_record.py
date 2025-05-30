from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DomainDnsCnameRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.domainDnsCnameRecord"] = Field(alias="@odata.type", default="#microsoft.graph.domainDnsCnameRecord")
	isOptional: Optional[bool] = Field(alias="isOptional", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	recordType: Optional[str] = Field(alias="recordType", default=None,)
	supportedService: Optional[str] = Field(alias="supportedService", default=None,)
	ttl: Optional[int] = Field(alias="ttl", default=None,)
	canonicalName: Optional[str] = Field(alias="canonicalName", default=None,)

