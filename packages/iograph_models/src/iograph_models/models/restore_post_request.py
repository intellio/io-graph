from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePostRequest(BaseModel):
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	name: Optional[str] = Field(default=None,alias="name",)

from .item_reference import ItemReference

