from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DproductPostRequest(BaseModel):
	database: Optional[str] = Field(alias="database", default=None,)
	field: Optional[str] = Field(alias="field", default=None,)
	criteria: Optional[str] = Field(alias="criteria", default=None,)


