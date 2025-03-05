from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeOff(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	draftTimeOff: Optional[TimeOffItem] = Field(alias="draftTimeOff",default=None,)
	isStagedForDeletion: Optional[bool] = Field(alias="isStagedForDeletion",default=None,)
	sharedTimeOff: Optional[TimeOffItem] = Field(alias="sharedTimeOff",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .time_off_item import TimeOffItem
from .time_off_item import TimeOffItem

