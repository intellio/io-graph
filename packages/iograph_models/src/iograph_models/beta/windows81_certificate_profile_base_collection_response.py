from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Windows81CertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Windows81SCEPCertificateProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile

