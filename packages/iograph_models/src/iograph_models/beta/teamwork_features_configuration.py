from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkFeaturesConfiguration(BaseModel):
	emailToSendLogsAndFeedback: Optional[str] = Field(alias="emailToSendLogsAndFeedback",default=None,)
	isAutoScreenShareEnabled: Optional[bool] = Field(alias="isAutoScreenShareEnabled",default=None,)
	isBluetoothBeaconingEnabled: Optional[bool] = Field(alias="isBluetoothBeaconingEnabled",default=None,)
	isHideMeetingNamesEnabled: Optional[bool] = Field(alias="isHideMeetingNamesEnabled",default=None,)
	isSendLogsAndFeedbackEnabled: Optional[bool] = Field(alias="isSendLogsAndFeedbackEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


