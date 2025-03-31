from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PermissionsAnalyticsAggregation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionsAnalyticsAggregation"] = Field(alias="@odata.type",)
	aws: Optional[PermissionsAnalytics] = Field(alias="aws", default=None,)
	azure: Optional[PermissionsAnalytics] = Field(alias="azure", default=None,)
	gcp: Optional[PermissionsAnalytics] = Field(alias="gcp", default=None,)

from .permissions_analytics import PermissionsAnalytics
