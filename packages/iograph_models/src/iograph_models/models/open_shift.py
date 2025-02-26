from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OpenShift(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	draftOpenShift: Optional[OpenShiftItem] = Field(default=None,alias="draftOpenShift",)
	isStagedForDeletion: Optional[bool] = Field(default=None,alias="isStagedForDeletion",)
	schedulingGroupId: Optional[str] = Field(default=None,alias="schedulingGroupId",)
	sharedOpenShift: Optional[OpenShiftItem] = Field(default=None,alias="sharedOpenShift",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .open_shift_item import OpenShiftItem
from .open_shift_item import OpenShiftItem

