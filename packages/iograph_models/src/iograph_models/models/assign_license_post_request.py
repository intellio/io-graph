from __future__ import annotations
from uuid import UUID
from pydantic import BaseModel, Field


class Assign_licensePostRequest(BaseModel):
	addLicenses: list[AssignedLicense] = Field(alias="addLicenses",)
	removeLicenses: list[UUID] = Field(alias="removeLicenses",)

from .assigned_license import AssignedLicense

