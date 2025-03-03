from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Calendar(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedOnlineMeetingProviders: Optional[OnlineMeetingProviderType] = Field(default=None,alias="allowedOnlineMeetingProviders",)
	canEdit: Optional[bool] = Field(default=None,alias="canEdit",)
	canShare: Optional[bool] = Field(default=None,alias="canShare",)
	canViewPrivateItems: Optional[bool] = Field(default=None,alias="canViewPrivateItems",)
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	color: Optional[CalendarColor] = Field(default=None,alias="color",)
	defaultOnlineMeetingProvider: Optional[OnlineMeetingProviderType] = Field(default=None,alias="defaultOnlineMeetingProvider",)
	hexColor: Optional[str] = Field(default=None,alias="hexColor",)
	isDefaultCalendar: Optional[bool] = Field(default=None,alias="isDefaultCalendar",)
	isRemovable: Optional[bool] = Field(default=None,alias="isRemovable",)
	isTallyingResponses: Optional[bool] = Field(default=None,alias="isTallyingResponses",)
	name: Optional[str] = Field(default=None,alias="name",)
	owner: Optional[EmailAddress] = Field(default=None,alias="owner",)
	calendarPermissions: Optional[list[CalendarPermission]] = Field(default=None,alias="calendarPermissions",)
	calendarView: Optional[list[Event]] = Field(default=None,alias="calendarView",)
	events: Optional[list[Event]] = Field(default=None,alias="events",)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(default=None,alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="singleValueExtendedProperties",)

from .online_meeting_provider_type import OnlineMeetingProviderType
from .calendar_color import CalendarColor
from .online_meeting_provider_type import OnlineMeetingProviderType
from .email_address import EmailAddress
from .calendar_permission import CalendarPermission
from .event import Event
from .event import Event
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

