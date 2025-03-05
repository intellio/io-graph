from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Shift(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	draftShift: Optional[ShiftItem] = Field(default=None,alias="draftShift",)
	isStagedForDeletion: Optional[bool] = Field(default=None,alias="isStagedForDeletion",)
	schedulingGroupId: Optional[str] = Field(default=None,alias="schedulingGroupId",)
	sharedShift: Optional[ShiftItem] = Field(default=None,alias="sharedShift",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .shift_item import ShiftItem
from .shift_item import ShiftItem

