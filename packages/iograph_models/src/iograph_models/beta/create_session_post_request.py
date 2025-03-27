from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_sessionPostRequest(BaseModel):
	persistChanges: Optional[bool] = Field(alias="persistChanges", default=None,)


