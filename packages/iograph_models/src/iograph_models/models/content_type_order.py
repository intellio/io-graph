from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContentTypeOrder(BaseModel):
	default: Optional[bool] = Field(default=None,alias="default",)
	position: Optional[int] = Field(default=None,alias="position",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


