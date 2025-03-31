from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class Start_hold_musicPostRequest(BaseModel):
	customPrompt: Optional[Union[MediaPrompt]] = Field(alias="customPrompt", default=None,discriminator="odata_type", )
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)

from .media_prompt import MediaPrompt
