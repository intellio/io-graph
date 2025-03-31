from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Contract(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.contract"] = Field(alias="@odata.type", default="#microsoft.graph.contract")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	contractType: Optional[str] = Field(alias="contractType", default=None,)
	customerId: Optional[UUID] = Field(alias="customerId", default=None,)
	defaultDomainName: Optional[str] = Field(alias="defaultDomainName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

