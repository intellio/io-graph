from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ComplianceInformation(BaseModel):
	certificationControls: list[CertificationControl] = Field(alias="certificationControls",)
	certificationName: Optional[str] = Field(default=None,alias="certificationName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .certification_control import CertificationControl

