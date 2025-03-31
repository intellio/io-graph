from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows_defender_scanPostRequest(BaseModel):
	quickScan: Optional[bool] = Field(alias="quickScan", default=None,)

