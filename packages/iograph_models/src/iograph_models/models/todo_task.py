from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TodoTask(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	bodyLastModifiedDateTime: Optional[datetime] = Field(default=None,alias="bodyLastModifiedDateTime",)
	categories: Optional[list[str]] = Field(default=None,alias="categories",)
	completedDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="completedDateTime",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	dueDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="dueDateTime",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	importance: Optional[Importance] = Field(default=None,alias="importance",)
	isReminderOn: Optional[bool] = Field(default=None,alias="isReminderOn",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	recurrence: Optional[PatternedRecurrence] = Field(default=None,alias="recurrence",)
	reminderDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="reminderDateTime",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	status: Optional[TaskStatus] = Field(default=None,alias="status",)
	title: Optional[str] = Field(default=None,alias="title",)
	attachments: SerializeAsAny[Optional[list[AttachmentBase]]] = Field(default=None,alias="attachments",)
	attachmentSessions: Optional[list[AttachmentSession]] = Field(default=None,alias="attachmentSessions",)
	checklistItems: Optional[list[ChecklistItem]] = Field(default=None,alias="checklistItems",)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(default=None,alias="extensions",)
	linkedResources: Optional[list[LinkedResource]] = Field(default=None,alias="linkedResources",)

from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .importance import Importance
from .patterned_recurrence import PatternedRecurrence
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .task_status import TaskStatus
from .attachment_base import AttachmentBase
from .attachment_session import AttachmentSession
from .checklist_item import ChecklistItem
from .extension import Extension
from .linked_resource import LinkedResource

