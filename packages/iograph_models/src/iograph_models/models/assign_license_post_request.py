from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Assign_licensePostRequest(BaseModel):
	addLicenses: Optional[list[AssignedLicense]] = Field(default=None,alias="addLicenses",)
	removeLicenses: Optional[list[UUID]] = Field(default=None,alias="removeLicenses",)

from .assigned_license import AssignedLicense

