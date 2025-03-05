from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeOffReason(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	code: Optional[str] = Field(default=None,alias="code",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	iconType: Optional[TimeOffReasonIconType] = Field(default=None,alias="iconType",)
	isActive: Optional[bool] = Field(default=None,alias="isActive",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .time_off_reason_icon_type import TimeOffReasonIconType

