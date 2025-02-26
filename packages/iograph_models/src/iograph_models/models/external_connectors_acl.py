from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsAcl(BaseModel):
	accessType: Optional[ExternalConnectorsAccessType] = Field(default=None,alias="accessType",)
	type: Optional[ExternalConnectorsAclType] = Field(default=None,alias="type",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_access_type import ExternalConnectorsAccessType
from .external_connectors_acl_type import ExternalConnectorsAclType

