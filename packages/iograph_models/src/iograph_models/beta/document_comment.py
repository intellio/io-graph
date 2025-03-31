from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DocumentComment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.documentComment"] = Field(alias="@odata.type",)
	content: Optional[str] = Field(alias="content", default=None,)
	replies: Optional[list[DocumentCommentReply]] = Field(alias="replies", default=None,)

from .document_comment_reply import DocumentCommentReply
