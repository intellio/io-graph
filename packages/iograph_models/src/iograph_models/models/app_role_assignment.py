from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AppRoleAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	appRoleId: Optional[UUID] = Field(default=None,alias="appRoleId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	principalDisplayName: Optional[str] = Field(default=None,alias="principalDisplayName",)
	principalId: Optional[UUID] = Field(default=None,alias="principalId",)
	principalType: Optional[str] = Field(default=None,alias="principalType",)
	resourceDisplayName: Optional[str] = Field(default=None,alias="resourceDisplayName",)
	resourceId: Optional[UUID] = Field(default=None,alias="resourceId",)


