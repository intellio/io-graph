from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringApplicationImpactSummary(BaseModel):
	impactedCount: Optional[str] = Field(alias="impactedCount",default=None,)
	impactedCountLimitExceeded: Optional[bool] = Field(alias="impactedCountLimitExceeded",default=None,)
	resourceType: Optional[str] = Field(alias="resourceType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	resourceSampling: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="resourceSampling",default=None,)

from .directory_object import DirectoryObject

