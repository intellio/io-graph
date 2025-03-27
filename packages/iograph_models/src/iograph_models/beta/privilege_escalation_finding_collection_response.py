from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegeEscalationFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[PrivilegeEscalationAwsResourceFinding, PrivilegeEscalationAwsRoleFinding, PrivilegeEscalationGcpServiceAccountFinding, PrivilegeEscalationUserFinding]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

