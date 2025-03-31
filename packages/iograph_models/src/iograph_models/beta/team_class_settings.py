from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamClassSettings(BaseModel):
	notifyGuardiansAboutAssignments: Optional[bool] = Field(alias="notifyGuardiansAboutAssignments", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

