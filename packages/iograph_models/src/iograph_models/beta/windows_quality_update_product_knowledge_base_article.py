from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsQualityUpdateProductKnowledgeBaseArticle(BaseModel):
	articleId: Optional[str] = Field(alias="articleId",default=None,)
	articleUrl: Optional[str] = Field(alias="articleUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


