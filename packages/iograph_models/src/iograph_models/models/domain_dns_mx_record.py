from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DomainDnsMxRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isOptional: Optional[bool] = Field(alias="isOptional",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	recordType: Optional[str] = Field(alias="recordType",default=None,)
	supportedService: Optional[str] = Field(alias="supportedService",default=None,)
	ttl: Optional[int] = Field(alias="ttl",default=None,)
	mailExchange: Optional[str] = Field(alias="mailExchange",default=None,)
	preference: Optional[int] = Field(alias="preference",default=None,)


