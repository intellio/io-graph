from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Ediscovery_apply_tagsPostRequest(BaseModel):
	tagsToAdd: Optional[list[EdiscoveryTag]] = Field(alias="tagsToAdd",default=None,)
	tagsToRemove: Optional[list[EdiscoveryTag]] = Field(alias="tagsToRemove",default=None,)

from .ediscovery_tag import EdiscoveryTag
from .ediscovery_tag import EdiscoveryTag

