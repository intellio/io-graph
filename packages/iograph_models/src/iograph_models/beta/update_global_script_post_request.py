from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_global_scriptPostRequest(BaseModel):
	version: Optional[str] = Field(alias="version", default=None,)


