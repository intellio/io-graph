from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionCalloutRequest(BaseModel):
	data: SerializeAsAny[Optional[CustomExtensionData]] = Field(alias="data",default=None,)
	source: Optional[str] = Field(alias="source",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .custom_extension_data import CustomExtensionData

