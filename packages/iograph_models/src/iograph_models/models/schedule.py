from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Schedule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	isActivitiesIncludedWhenCopyingShiftsEnabled: Optional[bool] = Field(default=None,alias="isActivitiesIncludedWhenCopyingShiftsEnabled",)
	offerShiftRequestsEnabled: Optional[bool] = Field(default=None,alias="offerShiftRequestsEnabled",)
	openShiftsEnabled: Optional[bool] = Field(default=None,alias="openShiftsEnabled",)
	provisionStatus: Optional[OperationStatus] = Field(default=None,alias="provisionStatus",)
	provisionStatusCode: Optional[str] = Field(default=None,alias="provisionStatusCode",)
	startDayOfWeek: Optional[DayOfWeek] = Field(default=None,alias="startDayOfWeek",)
	swapShiftsRequestsEnabled: Optional[bool] = Field(default=None,alias="swapShiftsRequestsEnabled",)
	timeClockEnabled: Optional[bool] = Field(default=None,alias="timeClockEnabled",)
	timeClockSettings: Optional[TimeClockSettings] = Field(default=None,alias="timeClockSettings",)
	timeOffRequestsEnabled: Optional[bool] = Field(default=None,alias="timeOffRequestsEnabled",)
	timeZone: Optional[str] = Field(default=None,alias="timeZone",)
	workforceIntegrationIds: Optional[list[str]] = Field(default=None,alias="workforceIntegrationIds",)
	dayNotes: Optional[list[DayNote]] = Field(default=None,alias="dayNotes",)
	offerShiftRequests: Optional[list[OfferShiftRequest]] = Field(default=None,alias="offerShiftRequests",)
	openShiftChangeRequests: Optional[list[OpenShiftChangeRequest]] = Field(default=None,alias="openShiftChangeRequests",)
	openShifts: Optional[list[OpenShift]] = Field(default=None,alias="openShifts",)
	schedulingGroups: Optional[list[SchedulingGroup]] = Field(default=None,alias="schedulingGroups",)
	shifts: Optional[list[Shift]] = Field(default=None,alias="shifts",)
	swapShiftsChangeRequests: Optional[list[SwapShiftsChangeRequest]] = Field(default=None,alias="swapShiftsChangeRequests",)
	timeCards: Optional[list[TimeCard]] = Field(default=None,alias="timeCards",)
	timeOffReasons: Optional[list[TimeOffReason]] = Field(default=None,alias="timeOffReasons",)
	timeOffRequests: Optional[list[TimeOffRequest]] = Field(default=None,alias="timeOffRequests",)
	timesOff: Optional[list[TimeOff]] = Field(default=None,alias="timesOff",)

from .operation_status import OperationStatus
from .day_of_week import DayOfWeek
from .time_clock_settings import TimeClockSettings
from .day_note import DayNote
from .offer_shift_request import OfferShiftRequest
from .open_shift_change_request import OpenShiftChangeRequest
from .open_shift import OpenShift
from .scheduling_group import SchedulingGroup
from .shift import Shift
from .swap_shifts_change_request import SwapShiftsChangeRequest
from .time_card import TimeCard
from .time_off_reason import TimeOffReason
from .time_off_request import TimeOffRequest
from .time_off import TimeOff

