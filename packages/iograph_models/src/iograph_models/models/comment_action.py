from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommentAction(BaseModel):
	isReply: Optional[bool] = Field(default=None,alias="isReply",)
	parentAuthor: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="parentAuthor",)
	participants: SerializeAsAny[Optional[list[IdentitySet]]] = Field(default=None,alias="participants",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

