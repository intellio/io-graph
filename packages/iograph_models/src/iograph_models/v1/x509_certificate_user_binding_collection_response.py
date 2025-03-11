from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateUserBindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[X509CertificateUserBinding]] = Field(alias="value",default=None,)

from .x509_certificate_user_binding import X509CertificateUserBinding

