from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MergePostRequest(BaseModel):
	across: Optional[bool] = Field(alias="across", default=None,)


