from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Extract_labelPostRequest(BaseModel):
	contentInfo: Optional[ContentInfo] = Field(alias="contentInfo",default=None,)

from .content_info import ContentInfo

