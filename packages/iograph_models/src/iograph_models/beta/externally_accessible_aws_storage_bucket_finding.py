from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExternallyAccessibleAwsStorageBucketFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externallyAccessibleAwsStorageBucketFinding"] = Field(alias="@odata.type", default="#microsoft.graph.externallyAccessibleAwsStorageBucketFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessibility: Optional[AwsAccessType | str] = Field(alias="accessibility", default=None,)
	accountsWithAccess: Optional[Union[AllAccountsWithAccess, EnumeratedAccountsWithAccess]] = Field(alias="accountsWithAccess", default=None,discriminator="odata_type", )
	storageBucket: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="storageBucket", default=None,discriminator="odata_type", )

from .aws_access_type import AwsAccessType
from .all_accounts_with_access import AllAccountsWithAccess
from .enumerated_accounts_with_access import EnumeratedAccountsWithAccess
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
