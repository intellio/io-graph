from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class DlpEvaluatePoliciesRequest(BaseModel):
	evaluationInput: Optional[Union[DlpEvaluationWindowsDevicesInput]] = Field(alias="evaluationInput", default=None,discriminator="odata_type", )
	notificationInfo: Optional[Union[DlpWindowsDevicesNotification]] = Field(alias="notificationInfo", default=None,discriminator="odata_type", )
	target: Optional[str] = Field(alias="target", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .dlp_evaluation_windows_devices_input import DlpEvaluationWindowsDevicesInput
from .dlp_windows_devices_notification import DlpWindowsDevicesNotification

