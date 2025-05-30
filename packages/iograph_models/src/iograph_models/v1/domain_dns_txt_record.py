from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DomainDnsTxtRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.domainDnsTxtRecord"] = Field(alias="@odata.type", default="#microsoft.graph.domainDnsTxtRecord")
	isOptional: Optional[bool] = Field(alias="isOptional", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	recordType: Optional[str] = Field(alias="recordType", default=None,)
	supportedService: Optional[str] = Field(alias="supportedService", default=None,)
	ttl: Optional[int] = Field(alias="ttl", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)

