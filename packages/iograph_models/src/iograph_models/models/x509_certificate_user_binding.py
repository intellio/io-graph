from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateUserBinding(BaseModel):
	priority: Optional[int] = Field(alias="priority",default=None,)
	trustAffinityLevel: Optional[str | X509CertificateAffinityLevel] = Field(alias="trustAffinityLevel",default=None,)
	userProperty: Optional[str] = Field(alias="userProperty",default=None,)
	x509CertificateField: Optional[str] = Field(alias="x509CertificateField",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .x509_certificate_affinity_level import X509CertificateAffinityLevel

