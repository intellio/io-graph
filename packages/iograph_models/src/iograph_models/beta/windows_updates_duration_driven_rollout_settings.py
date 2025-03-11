from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDurationDrivenRolloutSettings(BaseModel):
	durationBetweenOffers: Optional[str] = Field(alias="durationBetweenOffers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	durationUntilDeploymentEnd: Optional[str] = Field(alias="durationUntilDeploymentEnd",default=None,)


