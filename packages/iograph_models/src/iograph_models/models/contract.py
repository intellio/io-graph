from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Contract(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	contractType: Optional[str] = Field(default=None,alias="contractType",)
	customerId: Optional[UUID] = Field(default=None,alias="customerId",)
	defaultDomainName: Optional[str] = Field(default=None,alias="defaultDomainName",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)


