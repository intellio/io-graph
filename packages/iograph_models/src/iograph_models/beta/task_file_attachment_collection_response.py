from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TaskFileAttachmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TaskFileAttachment]] = Field(alias="value", default=None,)

from .task_file_attachment import TaskFileAttachment
