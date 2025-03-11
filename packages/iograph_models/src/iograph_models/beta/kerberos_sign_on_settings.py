from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class KerberosSignOnSettings(BaseModel):
	kerberosServicePrincipalName: Optional[str] = Field(alias="kerberosServicePrincipalName",default=None,)
	kerberosSignOnMappingAttributeType: Optional[KerberosSignOnMappingAttributeType | str] = Field(alias="kerberosSignOnMappingAttributeType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .kerberos_sign_on_mapping_attribute_type import KerberosSignOnMappingAttributeType

