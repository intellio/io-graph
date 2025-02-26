from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class ApiApplication(BaseModel):
	acceptMappedClaims: Optional[bool] = Field(default=None,alias="acceptMappedClaims",)
	knownClientApplications: list[Optional[UUID]] = Field(alias="knownClientApplications",)
	oauth2PermissionScopes: list[PermissionScope] = Field(alias="oauth2PermissionScopes",)
	preAuthorizedApplications: list[PreAuthorizedApplication] = Field(alias="preAuthorizedApplications",)
	requestedAccessTokenVersion: Optional[int] = Field(default=None,alias="requestedAccessTokenVersion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .permission_scope import PermissionScope
from .pre_authorized_application import PreAuthorizedApplication

