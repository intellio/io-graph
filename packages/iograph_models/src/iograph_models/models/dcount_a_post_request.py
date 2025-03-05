from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Dcount_aPostRequest(BaseModel):
	database: Optional[str] = Field(default=None,alias="database",)
	field: Optional[str] = Field(default=None,alias="field",)
	criteria: Optional[str] = Field(default=None,alias="criteria",)


