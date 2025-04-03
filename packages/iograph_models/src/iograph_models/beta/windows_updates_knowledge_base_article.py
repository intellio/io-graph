from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsUpdatesKnowledgeBaseArticle(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.knowledgeBaseArticle"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.knowledgeBaseArticle")
	url: Optional[str] = Field(alias="url", default=None,)

