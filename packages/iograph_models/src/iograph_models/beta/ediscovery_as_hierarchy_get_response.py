from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Ediscovery_as_hierarchyGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[EdiscoveryTag]] = Field(alias="value",default=None,)

from .ediscovery_tag import EdiscoveryTag

