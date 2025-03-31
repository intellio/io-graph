from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_extract_content_labelPostRequest(BaseModel):
	contentInfo: Optional[SecurityContentInfo] = Field(alias="contentInfo", default=None,)

from .security_content_info import SecurityContentInfo
