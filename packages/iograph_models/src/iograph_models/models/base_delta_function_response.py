from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BaseDeltaFunctionResponse(BaseModel):
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	odata_deltaLink: Optional[str] = Field(default=None,alias="@odata.deltaLink",)


