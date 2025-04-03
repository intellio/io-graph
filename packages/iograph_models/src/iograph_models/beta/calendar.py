from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class Calendar(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.calendar"] = Field(alias="@odata.type", default="#microsoft.graph.calendar")
	allowedOnlineMeetingProviders: Optional[list[OnlineMeetingProviderType | str]] = Field(alias="allowedOnlineMeetingProviders", default=None,)
	calendarGroupId: Optional[str] = Field(alias="calendarGroupId", default=None,)
	canEdit: Optional[bool] = Field(alias="canEdit", default=None,)
	canShare: Optional[bool] = Field(alias="canShare", default=None,)
	canViewPrivateItems: Optional[bool] = Field(alias="canViewPrivateItems", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	color: Optional[CalendarColor | str] = Field(alias="color", default=None,)
	defaultOnlineMeetingProvider: Optional[OnlineMeetingProviderType | str] = Field(alias="defaultOnlineMeetingProvider", default=None,)
	hexColor: Optional[str] = Field(alias="hexColor", default=None,)
	isDefaultCalendar: Optional[bool] = Field(alias="isDefaultCalendar", default=None,)
	isRemovable: Optional[bool] = Field(alias="isRemovable", default=None,)
	isShared: Optional[bool] = Field(alias="isShared", default=None,)
	isSharedWithMe: Optional[bool] = Field(alias="isSharedWithMe", default=None,)
	isTallyingResponses: Optional[bool] = Field(alias="isTallyingResponses", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	owner: Optional[Union[TypedEmailAddress]] = Field(alias="owner", default=None,discriminator="odata_type", )
	calendarPermissions: Optional[list[CalendarPermission]] = Field(alias="calendarPermissions", default=None,)
	calendarView: Optional[list[Event]] = Field(alias="calendarView", default=None,)
	events: Optional[list[Event]] = Field(alias="events", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .online_meeting_provider_type import OnlineMeetingProviderType
from .calendar_color import CalendarColor
from .typed_email_address import TypedEmailAddress
from .calendar_permission import CalendarPermission
from .event import Event
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
