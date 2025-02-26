from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookComment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	content: Optional[str] = Field(default=None,alias="content",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	replies: list[WorkbookCommentReply] = Field(alias="replies",)

from .workbook_comment_reply import WorkbookCommentReply

