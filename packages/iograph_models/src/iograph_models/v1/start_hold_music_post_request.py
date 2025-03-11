from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Start_hold_musicPostRequest(BaseModel):
	customPrompt: SerializeAsAny[Optional[Prompt]] = Field(alias="customPrompt",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)

from .prompt import Prompt

