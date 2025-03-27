from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class RequestorSettings(BaseModel):
	acceptRequests: Optional[bool] = Field(alias="acceptRequests", default=None,)
	allowedRequestors: Optional[list[Annotated[Union[ConnectedOrganizationMembers, ExternalSponsors, GroupMembers, InternalSponsors, RequestorManager, SingleUser, TargetUserSponsors],Field(discriminator="odata_type")]]] = Field(alias="allowedRequestors", default=None,)
	scopeType: Optional[str] = Field(alias="scopeType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .connected_organization_members import ConnectedOrganizationMembers
from .external_sponsors import ExternalSponsors
from .group_members import GroupMembers
from .internal_sponsors import InternalSponsors
from .requestor_manager import RequestorManager
from .single_user import SingleUser
from .target_user_sponsors import TargetUserSponsors

