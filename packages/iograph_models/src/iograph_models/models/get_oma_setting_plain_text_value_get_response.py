from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_oma_setting_plain_text_valueGetResponse(BaseModel):
	value: Optional[str] = Field(default=None,alias="value",)


