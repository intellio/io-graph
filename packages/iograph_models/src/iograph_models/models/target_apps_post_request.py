from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Target_appsPostRequest(BaseModel):
	apps: Optional[list[ManagedMobileApp]] = Field(default=None,alias="apps",)
	appGroupType: Optional[TargetedManagedAppGroupType] = Field(default=None,alias="appGroupType",)

from .managed_mobile_app import ManagedMobileApp
from .targeted_managed_app_group_type import TargetedManagedAppGroupType

