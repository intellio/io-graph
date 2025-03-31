from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeletedTeam(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deletedTeam"] = Field(alias="@odata.type",)
	channels: Optional[list[Channel]] = Field(alias="channels", default=None,)

from .channel import Channel
