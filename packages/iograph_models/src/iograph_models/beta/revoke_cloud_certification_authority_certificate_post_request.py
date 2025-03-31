from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Revoke_cloud_certification_authority_certificatePostRequest(BaseModel):
	certificationAuthorityVersion: Optional[int] = Field(alias="certificationAuthorityVersion", default=None,)

