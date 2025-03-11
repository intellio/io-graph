from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryEdiscoveryroot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cases: Optional[list[EdiscoveryCase]] = Field(alias="cases",default=None,)

from .ediscovery_case import EdiscoveryCase

