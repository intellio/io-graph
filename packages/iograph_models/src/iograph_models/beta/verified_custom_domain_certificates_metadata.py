from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiedCustomDomainCertificatesMetadata(BaseModel):
	expiryDate: Optional[datetime] = Field(alias="expiryDate", default=None,)
	issueDate: Optional[datetime] = Field(alias="issueDate", default=None,)
	issuerName: Optional[str] = Field(alias="issuerName", default=None,)
	subjectName: Optional[str] = Field(alias="subjectName", default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


