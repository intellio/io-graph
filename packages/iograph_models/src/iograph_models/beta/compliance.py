from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Compliance(BaseModel):
	ediscovery: Optional[EdiscoveryEdiscoveryroot] = Field(alias="ediscovery", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .ediscovery_ediscoveryroot import EdiscoveryEdiscoveryroot
