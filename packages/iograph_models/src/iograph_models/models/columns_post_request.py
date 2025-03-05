from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ColumnsPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)


