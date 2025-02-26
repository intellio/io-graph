from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Play_promptPostRequest(BaseModel):
	prompts: list[Prompt] = Field(alias="prompts",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)

from .prompt import Prompt

