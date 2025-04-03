from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DocumentCommentReply(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.documentCommentReply"] = Field(alias="@odata.type", default="#microsoft.graph.documentCommentReply")
	content: Optional[str] = Field(alias="content", default=None,)
	location: Optional[str] = Field(alias="location", default=None,)

