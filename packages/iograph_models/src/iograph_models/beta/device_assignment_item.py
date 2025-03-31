from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceAssignmentItem(BaseModel):
	assignmentItemActionIntent: Optional[DeviceAssignmentItemIntent | str] = Field(alias="assignmentItemActionIntent", default=None,)
	assignmentItemActionStatus: Optional[DeviceAssignmentItemStatus | str] = Field(alias="assignmentItemActionStatus", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	intentActionMessage: Optional[str] = Field(alias="intentActionMessage", default=None,)
	itemDisplayName: Optional[str] = Field(alias="itemDisplayName", default=None,)
	itemId: Optional[str] = Field(alias="itemId", default=None,)
	itemSubTypeDisplayName: Optional[str] = Field(alias="itemSubTypeDisplayName", default=None,)
	itemType: Optional[DeviceAssignmentItemType | str] = Field(alias="itemType", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_assignment_item_intent import DeviceAssignmentItemIntent
from .device_assignment_item_status import DeviceAssignmentItemStatus
from .device_assignment_item_type import DeviceAssignmentItemType
