from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class KeyRealValuePair(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)
	odata_type: Literal["#microsoft.graph.keyRealValuePair"] = Field(alias="@odata.type", default="#microsoft.graph.keyRealValuePair")
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
