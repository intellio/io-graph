from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DomainDnsUnavailableRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isOptional: Optional[bool] = Field(default=None,alias="isOptional",)
	label: Optional[str] = Field(default=None,alias="label",)
	recordType: Optional[str] = Field(default=None,alias="recordType",)
	supportedService: Optional[str] = Field(default=None,alias="supportedService",)
	ttl: Optional[int] = Field(default=None,alias="ttl",)
	description: Optional[str] = Field(default=None,alias="description",)


