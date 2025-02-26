from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFileHashCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityFileHash] = Field(alias="value",)

from .security_file_hash import SecurityFileHash

