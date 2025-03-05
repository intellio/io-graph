from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedPermissionClassification(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	classification: Optional[str | PermissionClassificationType] = Field(alias="classification",default=None,)
	permissionId: Optional[str] = Field(alias="permissionId",default=None,)
	permissionName: Optional[str] = Field(alias="permissionName",default=None,)

from .permission_classification_type import PermissionClassificationType

