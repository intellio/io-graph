from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamTemplate"] = Field(alias="@odata.type",)
	definitions: Optional[list[TeamTemplateDefinition]] = Field(alias="definitions", default=None,)

from .team_template_definition import TeamTemplateDefinition
