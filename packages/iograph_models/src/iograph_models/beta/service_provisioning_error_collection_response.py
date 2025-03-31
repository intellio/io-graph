from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class ServiceProvisioningErrorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[ServiceProvisioningResourceError, ServiceProvisioningXmlError],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .service_provisioning_resource_error import ServiceProvisioningResourceError
from .service_provisioning_xml_error import ServiceProvisioningXmlError
