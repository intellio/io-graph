from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Document(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	comments: Optional[list[DocumentComment]] = Field(alias="comments", default=None,)

from .document_comment import DocumentComment

