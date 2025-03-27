from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeprovisionPostRequest(BaseModel):
	deprovisionReason: Optional[str] = Field(alias="deprovisionReason", default=None,)


