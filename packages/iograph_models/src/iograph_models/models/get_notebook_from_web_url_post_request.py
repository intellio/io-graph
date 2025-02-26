from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_notebook_from_web_urlPostRequest(BaseModel):
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)


