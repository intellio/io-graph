from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemBody(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	contentType: Optional[BodyType] = Field(default=None,alias="contentType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .body_type import BodyType

