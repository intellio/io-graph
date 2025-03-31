from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Scoped_for_resource_with_resourceGetResponse(BaseModel):
	value: Optional[bool] = Field(alias="value", default=None,)

