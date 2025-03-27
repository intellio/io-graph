from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class RoleAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceAndAppManagementRoleAssignment]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment

