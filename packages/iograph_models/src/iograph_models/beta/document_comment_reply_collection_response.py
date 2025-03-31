from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DocumentCommentReplyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DocumentCommentReply]] = Field(alias="value", default=None,)

from .document_comment_reply import DocumentCommentReply
