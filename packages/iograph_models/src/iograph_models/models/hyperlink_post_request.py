from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class HyperlinkPostRequest(BaseModel):
	linkLocation: Optional[str] = Field(default=None,alias="linkLocation",)
	friendlyName: Optional[str] = Field(default=None,alias="friendlyName",)


