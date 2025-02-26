from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SchedulingGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	code: Optional[str] = Field(default=None,alias="code",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isActive: Optional[bool] = Field(default=None,alias="isActive",)
	userIds: list[Optional[str]] = Field(alias="userIds",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

