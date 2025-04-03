from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Program(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.program"] = Field(alias="@odata.type", default="#microsoft.graph.program")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	controls: Optional[list[ProgramControl]] = Field(alias="controls", default=None,)

from .program_control import ProgramControl
