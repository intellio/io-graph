from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookComment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookComment"] = Field(alias="@odata.type", default="#microsoft.graph.workbookComment")
	content: Optional[str] = Field(alias="content", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	replies: Optional[list[WorkbookCommentReply]] = Field(alias="replies", default=None,)
	task: Optional[WorkbookDocumentTask] = Field(alias="task", default=None,)

from .workbook_comment_reply import WorkbookCommentReply
from .workbook_document_task import WorkbookDocumentTask
