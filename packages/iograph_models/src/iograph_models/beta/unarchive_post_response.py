from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnarchivePostResponse(BaseModel):
	value: Optional[bool] = Field(alias="value", default=None,)


