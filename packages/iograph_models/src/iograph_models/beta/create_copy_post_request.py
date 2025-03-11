from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_copyPostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)


