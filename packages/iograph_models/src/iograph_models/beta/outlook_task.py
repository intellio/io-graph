from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OutlookTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.outlookTask"] = Field(alias="@odata.type", default="#microsoft.graph.outlookTask")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	completedDateTime: Optional[DateTimeTimeZone] = Field(alias="completedDateTime", default=None,)
	dueDateTime: Optional[DateTimeTimeZone] = Field(alias="dueDateTime", default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	importance: Optional[Importance | str] = Field(alias="importance", default=None,)
	isReminderOn: Optional[bool] = Field(alias="isReminderOn", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence", default=None,)
	reminderDateTime: Optional[DateTimeTimeZone] = Field(alias="reminderDateTime", default=None,)
	sensitivity: Optional[Sensitivity | str] = Field(alias="sensitivity", default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime", default=None,)
	status: Optional[TaskStatus | str] = Field(alias="status", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment]],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .importance import Importance
from .patterned_recurrence import PatternedRecurrence
from .date_time_time_zone import DateTimeTimeZone
from .sensitivity import Sensitivity
from .date_time_time_zone import DateTimeTimeZone
from .task_status import TaskStatus
from .file_attachment import FileAttachment
from .item_attachment import ItemAttachment
from .reference_attachment import ReferenceAttachment
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

