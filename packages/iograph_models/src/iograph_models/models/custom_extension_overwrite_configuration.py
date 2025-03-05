from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionOverwriteConfiguration(BaseModel):
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(alias="clientConfiguration",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .custom_extension_client_configuration import CustomExtensionClientConfiguration

