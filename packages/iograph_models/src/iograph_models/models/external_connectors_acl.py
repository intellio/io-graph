from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsAcl(BaseModel):
	accessType: Optional[str | ExternalConnectorsAccessType] = Field(alias="accessType",default=None,)
	type: Optional[str | ExternalConnectorsAclType] = Field(alias="type",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_connectors_access_type import ExternalConnectorsAccessType
from .external_connectors_acl_type import ExternalConnectorsAclType

