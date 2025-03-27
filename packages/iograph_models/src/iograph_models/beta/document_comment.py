from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentComment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	replies: Optional[list[DocumentCommentReply]] = Field(alias="replies", default=None,)

from .document_comment_reply import DocumentCommentReply

