from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Upload_certificatePostRequest(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)

