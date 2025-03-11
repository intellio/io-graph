from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsCreepIndex(BaseModel):
	score: Optional[int] = Field(alias="score",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


