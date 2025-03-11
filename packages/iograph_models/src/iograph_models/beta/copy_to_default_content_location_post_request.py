from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Copy_to_default_content_locationPostRequest(BaseModel):
	sourceFile: Optional[ItemReference] = Field(alias="sourceFile",default=None,)
	destinationFileName: Optional[str] = Field(alias="destinationFileName",default=None,)

from .item_reference import ItemReference

