from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Change_cloud_certification_authority_statusPostRequest(BaseModel):
	certificationAuthorityStatus: Optional[CloudCertificationAuthorityStatus | str] = Field(alias="certificationAuthorityStatus", default=None,)
	certificationAuthorityVersion: Optional[int] = Field(alias="certificationAuthorityVersion", default=None,)

from .cloud_certification_authority_status import CloudCertificationAuthorityStatus
