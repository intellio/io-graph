from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionCalloutResponse(BaseModel):
	data: SerializeAsAny[Optional[CustomExtensionData]] = Field(default=None,alias="data",)
	source: Optional[str] = Field(default=None,alias="source",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .custom_extension_data import CustomExtensionData

