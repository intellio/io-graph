from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DirectSharingAbilities(BaseModel):
	addExistingExternalUsers: Optional[SharingOperationStatus] = Field(alias="addExistingExternalUsers", default=None,)
	addInternalUsers: Optional[SharingOperationStatus] = Field(alias="addInternalUsers", default=None,)
	addNewExternalUsers: Optional[SharingOperationStatus] = Field(alias="addNewExternalUsers", default=None,)
	requestGrantAccess: Optional[SharingOperationStatus] = Field(alias="requestGrantAccess", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus
from .sharing_operation_status import SharingOperationStatus

