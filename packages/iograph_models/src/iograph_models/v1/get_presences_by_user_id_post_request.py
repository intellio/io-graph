from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_presences_by_user_idPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(alias="ids", default=None,)


