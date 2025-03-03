from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OsVersionCountCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OsVersionCount]] = Field(default=None,alias="value",)

from .os_version_count import OsVersionCount

