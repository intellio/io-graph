from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ComplianceInformation(BaseModel):
	certificationControls: Optional[list[CertificationControl]] = Field(alias="certificationControls", default=None,)
	certificationName: Optional[str] = Field(alias="certificationName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .certification_control import CertificationControl

