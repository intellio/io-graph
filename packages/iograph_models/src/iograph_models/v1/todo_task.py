from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TodoTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	bodyLastModifiedDateTime: Optional[datetime] = Field(alias="bodyLastModifiedDateTime", default=None,)
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	completedDateTime: Optional[DateTimeTimeZone] = Field(alias="completedDateTime", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dueDateTime: Optional[DateTimeTimeZone] = Field(alias="dueDateTime", default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	importance: Optional[Importance | str] = Field(alias="importance", default=None,)
	isReminderOn: Optional[bool] = Field(alias="isReminderOn", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence", default=None,)
	reminderDateTime: Optional[DateTimeTimeZone] = Field(alias="reminderDateTime", default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime", default=None,)
	status: Optional[TaskStatus | str] = Field(alias="status", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	attachments: Optional[list[Annotated[Union[TaskFileAttachment],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	attachmentSessions: Optional[list[AttachmentSession]] = Field(alias="attachmentSessions", default=None,)
	checklistItems: Optional[list[ChecklistItem]] = Field(alias="checklistItems", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	linkedResources: Optional[list[LinkedResource]] = Field(alias="linkedResources", default=None,)

from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .importance import Importance
from .patterned_recurrence import PatternedRecurrence
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .task_status import TaskStatus
from .task_file_attachment import TaskFileAttachment
from .attachment_session import AttachmentSession
from .checklist_item import ChecklistItem
from .open_type_extension import OpenTypeExtension
from .linked_resource import LinkedResource

