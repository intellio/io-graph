from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Json(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


