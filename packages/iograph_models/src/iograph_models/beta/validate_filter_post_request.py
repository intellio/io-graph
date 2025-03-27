from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_filterPostRequest(BaseModel):
	deviceAndAppManagementAssignmentFilter: Optional[Union[PayloadCompatibleAssignmentFilter]] = Field(alias="deviceAndAppManagementAssignmentFilter", default=None,discriminator="odata_type", )

from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter

