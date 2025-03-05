from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Add_groupPostRequest(BaseModel):
	groupId: Optional[str] = Field(alias="groupId",default=None,)


