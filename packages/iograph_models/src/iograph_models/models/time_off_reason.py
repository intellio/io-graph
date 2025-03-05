from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeOffReason(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	code: Optional[str] = Field(alias="code",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	iconType: Optional[str | TimeOffReasonIconType] = Field(alias="iconType",default=None,)
	isActive: Optional[bool] = Field(alias="isActive",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .time_off_reason_icon_type import TimeOffReasonIconType

