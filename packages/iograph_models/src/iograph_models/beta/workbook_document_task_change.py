from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WorkbookDocumentTaskChange(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookDocumentTaskChange"] = Field(alias="@odata.type", default="#microsoft.graph.workbookDocumentTaskChange")
	assignee: Optional[WorkbookEmailIdentity] = Field(alias="assignee", default=None,)
	changedBy: Optional[WorkbookEmailIdentity] = Field(alias="changedBy", default=None,)
	commentId: Optional[str] = Field(alias="commentId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime", default=None,)
	percentComplete: Optional[int] = Field(alias="percentComplete", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	undoChangeId: Optional[str] = Field(alias="undoChangeId", default=None,)

from .workbook_email_identity import WorkbookEmailIdentity
