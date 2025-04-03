from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DelegatedPermissionClassification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.delegatedPermissionClassification"] = Field(alias="@odata.type", default="#microsoft.graph.delegatedPermissionClassification")
	classification: Optional[PermissionClassificationType | str] = Field(alias="classification", default=None,)
	permissionId: Optional[str] = Field(alias="permissionId", default=None,)
	permissionName: Optional[str] = Field(alias="permissionName", default=None,)

from .permission_classification_type import PermissionClassificationType
