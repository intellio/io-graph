from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppCatalogs(BaseModel):
	teamsApps: Optional[list[TeamsApp]] = Field(alias="teamsApps", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_app import TeamsApp

