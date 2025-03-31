from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnOtpSendCustomExtensionHandler(BaseModel):
	odata_type: Literal["#microsoft.graph.onOtpSendCustomExtensionHandler"] = Field(alias="@odata.type", default="#microsoft.graph.onOtpSendCustomExtensionHandler")
	configuration: Optional[CustomExtensionOverwriteConfiguration] = Field(alias="configuration", default=None,)
	customExtension: Optional[OnOtpSendCustomExtension] = Field(alias="customExtension", default=None,)

from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
from .on_otp_send_custom_extension import OnOtpSendCustomExtension
