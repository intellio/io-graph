from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LinkRoleAbilities(BaseModel):
	addExistingExternalUsers: Optional[SharingOperationStatus] = Field(alias="addExistingExternalUsers", default=None,)
	addNewExternalUsers: Optional[SharingOperationStatus] = Field(alias="addNewExternalUsers", default=None,)
	applyVariants: Optional[SharingLinkVariants] = Field(alias="applyVariants", default=None,)
	createLink: Optional[SharingOperationStatus] = Field(alias="createLink", default=None,)
	deleteLink: Optional[SharingOperationStatus] = Field(alias="deleteLink", default=None,)
	linkAllowsExternalUsers: Optional[SharingOperationStatus] = Field(alias="linkAllowsExternalUsers", default=None,)
	linkExpiration: Optional[SharingLinkExpirationStatus] = Field(alias="linkExpiration", default=None,)
	retrieveLink: Optional[SharingOperationStatus] = Field(alias="retrieveLink", default=None,)
	updateLink: Optional[SharingOperationStatus] = Field(alias="updateLink", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_link_variants import SharingLinkVariants
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_link_expiration_status import SharingLinkExpirationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus

