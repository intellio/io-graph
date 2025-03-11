from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Check_member_objectsPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(alias="ids",default=None,)


