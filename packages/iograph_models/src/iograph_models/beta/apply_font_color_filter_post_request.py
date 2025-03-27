from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_font_color_filterPostRequest(BaseModel):
	color: Optional[str] = Field(alias="color", default=None,)


