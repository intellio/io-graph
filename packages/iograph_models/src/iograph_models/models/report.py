from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Report(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


