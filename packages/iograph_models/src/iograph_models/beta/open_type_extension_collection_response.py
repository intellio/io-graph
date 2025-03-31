from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OpenTypeExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OpenTypeExtension]] = Field(alias="value", default=None,)

from .open_type_extension import OpenTypeExtension
