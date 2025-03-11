from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionHandlerInstance(BaseModel):
	customExtensionId: Optional[str] = Field(alias="customExtensionId",default=None,)
	externalCorrelationId: Optional[str] = Field(alias="externalCorrelationId",default=None,)
	stage: Optional[AccessPackageCustomExtensionStage | str] = Field(alias="stage",default=None,)
	status: Optional[AccessPackageCustomExtensionHandlerStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
from .access_package_custom_extension_handler_status import AccessPackageCustomExtensionHandlerStatus

