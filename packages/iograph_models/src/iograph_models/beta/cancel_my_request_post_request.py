from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Cancel_my_requestPostRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)


