from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DomainDnsSrvRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.domainDnsSrvRecord"] = Field(alias="@odata.type",)
	isOptional: Optional[bool] = Field(alias="isOptional", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	recordType: Optional[str] = Field(alias="recordType", default=None,)
	supportedService: Optional[str] = Field(alias="supportedService", default=None,)
	ttl: Optional[int] = Field(alias="ttl", default=None,)
	nameTarget: Optional[str] = Field(alias="nameTarget", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	protocol: Optional[str] = Field(alias="protocol", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	weight: Optional[int] = Field(alias="weight", default=None,)

