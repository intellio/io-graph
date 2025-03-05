from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApiApplication(BaseModel):
	acceptMappedClaims: Optional[bool] = Field(default=None,alias="acceptMappedClaims",)
	knownClientApplications: Optional[list[UUID]] = Field(default=None,alias="knownClientApplications",)
	oauth2PermissionScopes: Optional[list[PermissionScope]] = Field(default=None,alias="oauth2PermissionScopes",)
	preAuthorizedApplications: Optional[list[PreAuthorizedApplication]] = Field(default=None,alias="preAuthorizedApplications",)
	requestedAccessTokenVersion: Optional[int] = Field(default=None,alias="requestedAccessTokenVersion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .permission_scope import PermissionScope
from .pre_authorized_application import PreAuthorizedApplication

