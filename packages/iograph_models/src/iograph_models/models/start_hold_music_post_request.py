from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Start_hold_musicPostRequest(BaseModel):
	customPrompt: SerializeAsAny[Optional[Prompt]] = Field(default=None,alias="customPrompt",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)

from .prompt import Prompt

