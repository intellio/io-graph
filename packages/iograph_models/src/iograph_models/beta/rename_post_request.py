from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RenamePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)


