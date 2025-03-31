from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EdiscoveryEdiscoveryroot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ediscovery.ediscoveryroot"] = Field(alias="@odata.type",)
	cases: Optional[list[EdiscoveryCase]] = Field(alias="cases", default=None,)

from .ediscovery_case import EdiscoveryCase
