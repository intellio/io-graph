from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OsVersionCountCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OsVersionCount]] = Field(alias="value", default=None,)

from .os_version_count import OsVersionCount
