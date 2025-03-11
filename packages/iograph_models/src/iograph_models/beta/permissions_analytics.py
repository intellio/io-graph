from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsAnalytics(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	findings: SerializeAsAny[Optional[list[Finding]]] = Field(alias="findings",default=None,)
	permissionsCreepIndexDistributions: Optional[list[PermissionsCreepIndexDistribution]] = Field(alias="permissionsCreepIndexDistributions",default=None,)

from .finding import Finding
from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

