from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Cancel_media_processingPostRequest(BaseModel):
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)

