from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomExtensionOverwriteConfiguration(BaseModel):
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(default=None,alias="clientConfiguration",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .custom_extension_client_configuration import CustomExtensionClientConfiguration

