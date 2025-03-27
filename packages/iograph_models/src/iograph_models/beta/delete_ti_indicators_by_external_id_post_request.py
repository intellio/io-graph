from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Delete_ti_indicators_by_external_idPostRequest(BaseModel):
	value: Optional[list[str]] = Field(alias="value", default=None,)


