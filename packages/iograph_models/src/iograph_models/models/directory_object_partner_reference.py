from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DirectoryObjectPartnerReference(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalPartnerTenantId: Optional[UUID] = Field(default=None,alias="externalPartnerTenantId",)
	objectType: Optional[str] = Field(default=None,alias="objectType",)


