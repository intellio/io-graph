from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TimeOff(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	draftTimeOff: Optional[TimeOffItem] = Field(default=None,alias="draftTimeOff",)
	isStagedForDeletion: Optional[bool] = Field(default=None,alias="isStagedForDeletion",)
	sharedTimeOff: Optional[TimeOffItem] = Field(default=None,alias="sharedTimeOff",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .time_off_item import TimeOffItem
from .time_off_item import TimeOffItem

