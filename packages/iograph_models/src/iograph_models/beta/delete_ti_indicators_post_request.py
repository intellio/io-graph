from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Delete_ti_indicatorsPostRequest(BaseModel):
	value: Optional[list[str]] = Field(alias="value", default=None,)

