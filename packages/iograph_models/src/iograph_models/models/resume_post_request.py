from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResumePostRequest(BaseModel):
	source: Optional[str] = Field(default=None,alias="source",)
	type: Optional[str] = Field(default=None,alias="type",)
	data: Optional[CustomExtensionData] = Field(default=None,alias="data",)

from .custom_extension_data import CustomExtensionData

