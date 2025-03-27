from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePostRequest(BaseModel):
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)

from .item_reference import ItemReference

