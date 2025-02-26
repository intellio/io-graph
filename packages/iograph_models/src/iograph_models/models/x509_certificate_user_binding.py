from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateUserBinding(BaseModel):
	priority: Optional[int] = Field(default=None,alias="priority",)
	trustAffinityLevel: Optional[X509CertificateAffinityLevel] = Field(default=None,alias="trustAffinityLevel",)
	userProperty: Optional[str] = Field(default=None,alias="userProperty",)
	x509CertificateField: Optional[str] = Field(default=None,alias="x509CertificateField",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .x509_certificate_affinity_level import X509CertificateAffinityLevel

