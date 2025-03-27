from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReactionsFacet(BaseModel):
	commentCount: Optional[int] = Field(alias="commentCount", default=None,)
	likeCount: Optional[int] = Field(alias="likeCount", default=None,)
	shareCount: Optional[int] = Field(alias="shareCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


