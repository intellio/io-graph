from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_cell_color_filterPostRequest(BaseModel):
	color: Optional[str] = Field(default=None,alias="color",)


