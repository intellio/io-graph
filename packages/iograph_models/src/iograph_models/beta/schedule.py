from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Schedule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activitiesIncludedWhenCopyingShiftsEnabled: Optional[bool] = Field(alias="activitiesIncludedWhenCopyingShiftsEnabled", default=None,)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	isActivitiesIncludedWhenCopyingShiftsEnabled: Optional[bool] = Field(alias="isActivitiesIncludedWhenCopyingShiftsEnabled", default=None,)
	isCrossLocationShiftRequestApprovalRequired: Optional[bool] = Field(alias="isCrossLocationShiftRequestApprovalRequired", default=None,)
	isCrossLocationShiftsEnabled: Optional[bool] = Field(alias="isCrossLocationShiftsEnabled", default=None,)
	offerShiftRequestsEnabled: Optional[bool] = Field(alias="offerShiftRequestsEnabled", default=None,)
	openShiftsEnabled: Optional[bool] = Field(alias="openShiftsEnabled", default=None,)
	provisionStatus: Optional[OperationStatus | str] = Field(alias="provisionStatus", default=None,)
	provisionStatusCode: Optional[str] = Field(alias="provisionStatusCode", default=None,)
	startDayOfWeek: Optional[DayOfWeek | str] = Field(alias="startDayOfWeek", default=None,)
	swapShiftsRequestsEnabled: Optional[bool] = Field(alias="swapShiftsRequestsEnabled", default=None,)
	timeClockEnabled: Optional[bool] = Field(alias="timeClockEnabled", default=None,)
	timeClockSettings: Optional[TimeClockSettings] = Field(alias="timeClockSettings", default=None,)
	timeOffRequestsEnabled: Optional[bool] = Field(alias="timeOffRequestsEnabled", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)
	workforceIntegrationIds: Optional[list[str]] = Field(alias="workforceIntegrationIds", default=None,)
	dayNotes: Optional[list[DayNote]] = Field(alias="dayNotes", default=None,)
	offerShiftRequests: Optional[list[Annotated[Union[SwapShiftsChangeRequest],Field(discriminator="odata_type")]]] = Field(alias="offerShiftRequests", default=None,)
	openShiftChangeRequests: Optional[list[OpenShiftChangeRequest]] = Field(alias="openShiftChangeRequests", default=None,)
	openShifts: Optional[list[OpenShift]] = Field(alias="openShifts", default=None,)
	schedulingGroups: Optional[list[SchedulingGroup]] = Field(alias="schedulingGroups", default=None,)
	shifts: Optional[list[Shift]] = Field(alias="shifts", default=None,)
	shiftsRoleDefinitions: Optional[list[ShiftsRoleDefinition]] = Field(alias="shiftsRoleDefinitions", default=None,)
	swapShiftsChangeRequests: Optional[list[SwapShiftsChangeRequest]] = Field(alias="swapShiftsChangeRequests", default=None,)
	timeCards: Optional[list[TimeCard]] = Field(alias="timeCards", default=None,)
	timeOffReasons: Optional[list[TimeOffReason]] = Field(alias="timeOffReasons", default=None,)
	timeOffRequests: Optional[list[TimeOffRequest]] = Field(alias="timeOffRequests", default=None,)
	timesOff: Optional[list[TimeOff]] = Field(alias="timesOff", default=None,)

from .operation_status import OperationStatus
from .day_of_week import DayOfWeek
from .time_clock_settings import TimeClockSettings
from .day_note import DayNote
from .swap_shifts_change_request import SwapShiftsChangeRequest
from .open_shift_change_request import OpenShiftChangeRequest
from .open_shift import OpenShift
from .scheduling_group import SchedulingGroup
from .shift import Shift
from .shifts_role_definition import ShiftsRoleDefinition
from .swap_shifts_change_request import SwapShiftsChangeRequest
from .time_card import TimeCard
from .time_off_reason import TimeOffReason
from .time_off_request import TimeOffRequest
from .time_off import TimeOff

