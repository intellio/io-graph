from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Export_personal_dataPostRequest(BaseModel):
	storageLocation: Optional[str] = Field(default=None,alias="storageLocation",)


