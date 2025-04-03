from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WorkbookDocumentTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookDocumentTask"] = Field(alias="@odata.type", default="#microsoft.graph.workbookDocumentTask")
	assignees: Optional[list[WorkbookEmailIdentity]] = Field(alias="assignees", default=None,)
	completedBy: Optional[WorkbookEmailIdentity] = Field(alias="completedBy", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[WorkbookEmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	percentComplete: Optional[int] = Field(alias="percentComplete", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	startAndDueDateTime: Optional[WorkbookDocumentTaskSchedule] = Field(alias="startAndDueDateTime", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	changes: Optional[list[WorkbookDocumentTaskChange]] = Field(alias="changes", default=None,)
	comment: Optional[WorkbookComment] = Field(alias="comment", default=None,)

from .workbook_email_identity import WorkbookEmailIdentity
from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
from .workbook_document_task_change import WorkbookDocumentTaskChange
from .workbook_comment import WorkbookComment
