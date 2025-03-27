from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_update_indexPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(alias="ids", default=None,)


