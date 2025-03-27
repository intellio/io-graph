from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class HybridAgentUpdaterConfiguration(BaseModel):
	allowUpdateConfigurationOverride: Optional[bool] = Field(alias="allowUpdateConfigurationOverride", default=None,)
	deferUpdateDateTime: Optional[datetime] = Field(alias="deferUpdateDateTime", default=None,)
	updateWindow: Optional[UpdateWindow] = Field(alias="updateWindow", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .update_window import UpdateWindow

