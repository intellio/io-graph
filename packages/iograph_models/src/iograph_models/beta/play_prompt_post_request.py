from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Play_promptPostRequest(BaseModel):
	prompts: SerializeAsAny[Optional[list[Prompt]]] = Field(alias="prompts",default=None,)
	loop: Optional[bool] = Field(alias="loop",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)

from .prompt import Prompt

