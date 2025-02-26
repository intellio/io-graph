from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommentAction(BaseModel):
	isReply: Optional[bool] = Field(default=None,alias="isReply",)
	parentAuthor: Optional[IdentitySet] = Field(default=None,alias="parentAuthor",)
	participants: list[IdentitySet] = Field(alias="participants",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

