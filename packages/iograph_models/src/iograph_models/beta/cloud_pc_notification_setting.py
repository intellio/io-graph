from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcNotificationSetting(BaseModel):
	restartPromptsDisabled: Optional[bool] = Field(alias="restartPromptsDisabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


