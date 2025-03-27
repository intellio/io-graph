from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDurationDrivenRolloutSettings(BaseModel):
	durationBetweenOffers: Optional[str] = Field(alias="durationBetweenOffers", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.durationDrivenRolloutSettings"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.durationDrivenRolloutSettings")
	durationUntilDeploymentEnd: Optional[str] = Field(alias="durationUntilDeploymentEnd", default=None,)


