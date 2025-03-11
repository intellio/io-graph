from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenShift(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	draftOpenShift: Optional[OpenShiftItem] = Field(alias="draftOpenShift",default=None,)
	isStagedForDeletion: Optional[bool] = Field(alias="isStagedForDeletion",default=None,)
	schedulingGroupId: Optional[str] = Field(alias="schedulingGroupId",default=None,)
	schedulingGroupInfo: Optional[SchedulingGroupInfo] = Field(alias="schedulingGroupInfo",default=None,)
	sharedOpenShift: Optional[OpenShiftItem] = Field(alias="sharedOpenShift",default=None,)
	teamInfo: Optional[ShiftsTeamInfo] = Field(alias="teamInfo",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .open_shift_item import OpenShiftItem
from .scheduling_group_info import SchedulingGroupInfo
from .open_shift_item import OpenShiftItem
from .shifts_team_info import ShiftsTeamInfo

