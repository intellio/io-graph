from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingLinkVariants(BaseModel):
	addressBarLinkPermission: Optional[SharingRole | str] = Field(alias="addressBarLinkPermission", default=None,)
	allowEmbed: Optional[SharingOperationStatus] = Field(alias="allowEmbed", default=None,)
	passwordProtected: Optional[SharingOperationStatus] = Field(alias="passwordProtected", default=None,)
	requiresAuthentication: Optional[SharingOperationStatus] = Field(alias="requiresAuthentication", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sharing_role import SharingRole
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus

