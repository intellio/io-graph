from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_user_owned_objectsPostRequest(BaseModel):
	userId: Optional[str] = Field(alias="userId", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)


