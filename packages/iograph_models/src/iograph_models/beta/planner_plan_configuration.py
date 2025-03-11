from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	buckets: Optional[list[PlannerPlanConfigurationBucketDefinition]] = Field(alias="buckets",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	localizations: Optional[list[PlannerPlanConfigurationLocalization]] = Field(alias="localizations",default=None,)

from .planner_plan_configuration_bucket_definition import PlannerPlanConfigurationBucketDefinition
from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization

