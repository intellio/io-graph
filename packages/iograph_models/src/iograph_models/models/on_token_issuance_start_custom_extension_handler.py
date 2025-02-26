from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnTokenIssuanceStartCustomExtensionHandler(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configuration: Optional[CustomExtensionOverwriteConfiguration] = Field(default=None,alias="configuration",)
	customExtension: Optional[OnTokenIssuanceStartCustomExtension] = Field(default=None,alias="customExtension",)

from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

