from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Document(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.document"] = Field(alias="@odata.type",)
	comments: Optional[list[DocumentComment]] = Field(alias="comments", default=None,)

from .document_comment import DocumentComment
