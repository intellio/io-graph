from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AppCatalogs(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appCatalogs"] = Field(alias="@odata.type",)
	teamsApps: Optional[list[TeamsApp]] = Field(alias="teamsApps", default=None,)

from .teams_app import TeamsApp
