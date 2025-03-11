from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessScenario(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	ownerAppIds: Optional[list[str]] = Field(alias="ownerAppIds",default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName",default=None,)
	planner: Optional[BusinessScenarioPlanner] = Field(alias="planner",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .business_scenario_planner import BusinessScenarioPlanner

