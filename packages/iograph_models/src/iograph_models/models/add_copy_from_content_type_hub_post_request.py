from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_copy_from_content_type_hubPostRequest(BaseModel):
	contentTypeId: Optional[str] = Field(default=None,alias="contentTypeId",)


