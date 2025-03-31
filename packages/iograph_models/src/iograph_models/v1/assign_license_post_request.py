from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class Assign_licensePostRequest(BaseModel):
	addLicenses: Optional[list[AssignedLicense]] = Field(alias="addLicenses", default=None,)
	removeLicenses: Optional[list[UUID]] = Field(alias="removeLicenses", default=None,)

from .assigned_license import AssignedLicense
