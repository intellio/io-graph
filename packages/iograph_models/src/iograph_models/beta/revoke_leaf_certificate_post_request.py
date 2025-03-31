from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Revoke_leaf_certificatePostRequest(BaseModel):
	leafCertificateId: Optional[str] = Field(alias="leafCertificateId", default=None,)

