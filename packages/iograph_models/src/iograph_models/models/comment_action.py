from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommentAction(BaseModel):
	isReply: Optional[bool] = Field(alias="isReply",default=None,)
	parentAuthor: SerializeAsAny[Optional[IdentitySet]] = Field(alias="parentAuthor",default=None,)
	participants: SerializeAsAny[Optional[list[IdentitySet]]] = Field(alias="participants",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

