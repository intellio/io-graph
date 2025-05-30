from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookCommentReply(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookCommentReply"] = Field(alias="@odata.type", default="#microsoft.graph.workbookCommentReply")
	content: Optional[str] = Field(alias="content", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)

