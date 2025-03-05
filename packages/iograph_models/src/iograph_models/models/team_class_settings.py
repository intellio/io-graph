from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamClassSettings(BaseModel):
	notifyGuardiansAboutAssignments: Optional[bool] = Field(default=None,alias="notifyGuardiansAboutAssignments",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


