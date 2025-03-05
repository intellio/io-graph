from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsSettings(BaseModel):
	configurationManagerDataConnectorConfigured: Optional[bool] = Field(default=None,alias="configurationManagerDataConnectorConfigured",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


