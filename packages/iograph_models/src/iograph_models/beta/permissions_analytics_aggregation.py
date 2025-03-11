from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsAnalyticsAggregation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	aws: Optional[PermissionsAnalytics] = Field(alias="aws",default=None,)
	azure: Optional[PermissionsAnalytics] = Field(alias="azure",default=None,)
	gcp: Optional[PermissionsAnalytics] = Field(alias="gcp",default=None,)

from .permissions_analytics import PermissionsAnalytics
from .permissions_analytics import PermissionsAnalytics
from .permissions_analytics import PermissionsAnalytics

