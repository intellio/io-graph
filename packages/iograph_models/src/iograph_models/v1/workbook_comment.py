from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookComment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	replies: Optional[list[WorkbookCommentReply]] = Field(alias="replies",default=None,)

from .workbook_comment_reply import WorkbookCommentReply

