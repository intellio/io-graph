from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Play_promptPostRequest(BaseModel):
	prompts: Optional[list[Annotated[Union[MediaPrompt],Field(discriminator="odata_type")]]] = Field(alias="prompts", default=None,)
	loop: Optional[bool] = Field(alias="loop", default=None,)
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)

from .media_prompt import MediaPrompt

