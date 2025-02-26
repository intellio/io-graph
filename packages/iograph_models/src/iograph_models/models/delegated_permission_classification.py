from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedPermissionClassification(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	classification: Optional[PermissionClassificationType] = Field(default=None,alias="classification",)
	permissionId: Optional[str] = Field(default=None,alias="permissionId",)
	permissionName: Optional[str] = Field(default=None,alias="permissionName",)

from .permission_classification_type import PermissionClassificationType

