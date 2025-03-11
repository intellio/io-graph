from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResumePostRequest(BaseModel):
	source: Optional[str] = Field(alias="source",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	data: SerializeAsAny[Optional[CustomExtensionData]] = Field(alias="data",default=None,)

from .custom_extension_data import CustomExtensionData

