from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Shift(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	draftShift: SerializeAsAny[Optional[ShiftItem]] = Field(alias="draftShift",default=None,)
	isStagedForDeletion: Optional[bool] = Field(alias="isStagedForDeletion",default=None,)
	schedulingGroupId: Optional[str] = Field(alias="schedulingGroupId",default=None,)
	schedulingGroupInfo: Optional[SchedulingGroupInfo] = Field(alias="schedulingGroupInfo",default=None,)
	sharedShift: SerializeAsAny[Optional[ShiftItem]] = Field(alias="sharedShift",default=None,)
	teamInfo: Optional[ShiftsTeamInfo] = Field(alias="teamInfo",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userInfo: Optional[ShiftsUserInfo] = Field(alias="userInfo",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .shift_item import ShiftItem
from .scheduling_group_info import SchedulingGroupInfo
from .shift_item import ShiftItem
from .shifts_team_info import ShiftsTeamInfo
from .shifts_user_info import ShiftsUserInfo

