from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReactionsFacet(BaseModel):
	commentCount: Optional[int] = Field(default=None,alias="commentCount",)
	likeCount: Optional[int] = Field(default=None,alias="likeCount",)
	shareCount: Optional[int] = Field(default=None,alias="shareCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


